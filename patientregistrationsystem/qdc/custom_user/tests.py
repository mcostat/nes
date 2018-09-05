# -*- coding: UTF-8 -*-
import re

from django.contrib.auth.models import Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.messages import get_messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.test import TestCase
from django.test.client import RequestFactory
from django.utils.http import int_to_base36
from django.utils.translation import ugettext as _

from custom_user.models import User, UserProfile
from custom_user.views import user_update

USER_USERNAME = 'myadmin'
USER_PWD = 'mypassword'
USER_NEW = 'user_new'
USER_VIEW = 'user_view'
USER_EDIT = 'user_edit'
PATTERN = '((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{6,20})'


class FormUserValidation(TestCase):

    user = ''

    def setUp(self):
        self.user = User.objects.create_superuser(username=USER_USERNAME, email='jenkins.neuromat@gmail.com',
                                                  password=USER_PWD)
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        profile, created = UserProfile.objects.get_or_create(user=self.user)
        profile.force_password_change = False
        profile.save()

        self.group = Group.objects.create(name='group')
        self.group.save()

        self.factory = RequestFactory()

        self.data = {'username': ['username'],
                     'first_name': ['General'],
                     'last_name': ['Test'],
                     'password': ['Adm!123'],
                     'password2': ['Adm!123'],
                     'groups': [self.group.id],
                     'email': ['email@test.com'],
                     'action': 'save'}

        logged = self.client.login(username=USER_USERNAME, password=USER_PWD)
        self.assertEqual(logged, True)

    def reset(self, user_added=None, request=None, domain_override=None,
              email_template_name='registration/password_reset_email.html',
              use_https=False, token_generator=default_token_generator):

        """Reset users password"""
        if not user_added.email:
            raise ValueError('Email address is required to send an email')

        if not domain_override:
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
        else:
            site_name = domain = domain_override

        loader.get_template(email_template_name)

        context = {
            'email': user_added.email,
            'domain': domain,
            'site_name': site_name,
            'uid': int_to_base36(user_added.id),
            'user': user_added,
            'token': token_generator.make_token(user_added),
            'protocol': use_https and 'https' or 'http',
        }

        subject_template_name = 'registration/password_reset_subject.txt'
        subject = loader.render_to_string(subject_template_name, context)

        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())

        # CHANGES START HERE!
        plain_text_content = loader.render_to_string(email_template_name.replace('with_html', 'plaintext'), context)
        html_content = loader.render_to_string(email_template_name, context)

        from django.core.mail import EmailMultiAlternatives

        msg = EmailMultiAlternatives(subject, plain_text_content, 'jenkins.neuromat@gmail.com', [user_added.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def test_user_invalid_username(self):
        self.data['username'] = ''
        self.data['login_enabled'] = True

        response = self.client.post(reverse(USER_NEW), self.data, follow=True)

        self.assertFormError(response, "form", "username", 'Este campo é obrigatório.')
        self.assertEqual(User.objects.filter(username='').count(), 0)

    def test_user_invalid_email(self):
        self.data['email'] = 'email@invalid.'
        self.data['login_enabled'] = True

        response = self.client.post(reverse(USER_NEW), self.data, follow=True)
        self.assertFormError(response, "form", "email", 'Informe um endereço de email válido.')
        self.assertEqual(User.objects.filter(username='').count(), 0)

    def test_user_email_already_registered(self):
        self.data['username'] = 'email_registered'
        self.data['first_name'] = 'Fulano'
        self.data['last_name'] = 'de Tal'
        self.data['email'] = 'jenkins.neuromat@gmail.com'
        self.data['login_enabled'] = False

        response = self.client.post(reverse(USER_NEW), self.data, follow=True)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         _('A researcher with this email address has already been registered before. '
                           'Please contact your system administrator if you want to reactivate this account.')
                         )
        self.assertEqual(User.objects.filter(username='email_registered').count(), 0)

        self.assertEqual(response.status_code, 200)

    def test_researcher_without_user(self):
        del self.user
        self.data['login_enabled'] = False

        response = self.client.post(reverse(USER_NEW), self.data)
        self.assertEqual(response.status_code, 302)

    def test_user_passwords_doesnt_match(self):
        user_pwd = 'test_pwd'
        self.data['username'] = user_pwd
        self.data['password'] = 'abc123'
        self.data['password2'] = 'acc123'
        self.data['login_enabled'] = True

        self.client.post(reverse(USER_NEW), self.data, follow=True)
        self.assertEqual(User.objects.filter(username=user_pwd).count(), 1)

    def test_user_empty_password(self):
        user_pwd = 'test_pwd_2'
        self.data['username'] = user_pwd
        self.data['password'] = ''
        self.data['login_enabled'] = True

        response = self.client.post(reverse(USER_NEW), self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "password", 'Este campo é obrigatório.')
        self.assertEqual(User.objects.filter(username=user_pwd).count(), 0)

    def test_user_create(self):
        username = 'test_username'
        self.data['username'] = username
        self.data['login_enabled'] = True

        response = self.client.post(reverse(USER_NEW), self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.filter(username=username).count(), 1)

    def test_user_create_mail_password_define(self):
        username = 'test_username'
        self.data['email'] = 'romulojosefranco@gmail.com'
        self.data['username'] = username
        self.data['login_enabled'] = True

        # Create an instance of a GET request.
        request = self.factory.get(reverse(USER_EDIT, args=[self.user.pk]))
        request.user = self.user

        response = self.client.post(reverse(USER_NEW), self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.filter(username=username).count(), 1)

        user_added = User.objects.filter(username=username).first()
        self.reset(user_added, request)

    def test_user_read(self):
        self.data['login_enabled'] = True
        # Create an instance of a GET request.
        request = self.factory.get(reverse(USER_EDIT, args=[self.user.pk]))
        request.user = self.user

        # Test view() as if it were deployed at /quiz/patient/%id
        response = user_update(request, user_id=self.user.pk)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse(USER_EDIT, args=[self.user.pk]), self.data)
        self.assertEqual(response.status_code, 302)

    def test_user_update_get(self):
        # Create an instance of a GET request.
        request = self.factory.get(reverse(USER_EDIT, args=[self.user.pk]))
        request.user = self.user

        # Test view() as if it were deployed at /quiz/patient/%id
        response = user_update(request, user_id=self.user.pk)
        self.assertEqual(response.status_code, 200)

    def test_user_update_post(self):
        first_name = 'test_username'
        self.data['first_name'] = first_name
        self.data['login_enabled'] = True

        response = self.client.post(reverse(USER_EDIT, args=(self.user.pk,)), self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.filter(id=self.user.pk).count(), 1)

        user_first_name = User.objects.filter(id=self.user.pk).first()

        self.assertEqual(user_first_name.first_name, first_name)

    def test_user_remove(self):
        user_str = 'user_remove'
        user_to_delete = User.objects.create_user(username=user_str, email='test@delete.com',
                                                  password='Del!123')
        user_to_delete.is_staff = True
        user_to_delete.is_superuser = True
        user_to_delete.is_active = True
        user_to_delete.save()
        self.assertEqual(User.objects.filter(username=user_str).count(), 1)

        self.data['action'] = 'remove'

        response = self.client.post(reverse(USER_EDIT, args=(user_to_delete.pk,)), self.data, follow=True)

        self.assertEqual(response.status_code, 200)
        user_to_delete = get_object_or_404(User, pk=user_to_delete.pk)
        self.assertEqual(user_to_delete.is_active, False)

        # Create an instance of a GET request.
        request = self.factory.get(reverse(USER_EDIT, args=[user_to_delete.pk, ]))
        request.user = self.user

        response = user_update(request, user_id=user_to_delete.pk)
        self.assertEqual(response, None)

    def test_create_researcher_without_system_access(self):
        username = 'fulano@detal.com'
        self.data['first_name'] = 'Fulano'
        self.data['last_name'] = 'de Tal'
        self.data['email'] = 'fulano@detal.com'
        self.data['username'] = username
        self.data['login_enabled'] = False
        self.client.post(reverse(USER_NEW), self.data)

        fulano = User.objects.get(username=username)
        self.assertTrue(fulano.is_active)
        self.assertFalse(fulano.has_usable_password())

    def test_remove_researcher_without_system_access(self):
        username = 'fulano@detal.com'
        self.data['first_name'] = 'Fulano'
        self.data['last_name'] = 'de Tal'
        self.data['email'] = 'fulano@detal.com'
        self.data['username'] = username
        self.data['login_enabled'] = False
        self.client.post(reverse(USER_NEW), self.data)

        resercher = User.objects.get(username=username)
        self.data['action'] = 'remove'
        response = self.client.post(reverse(USER_VIEW, args=(resercher.pk,)), self.data, follow=True)
        self.assertEqual(response.status_code, 200)


class PasswordPattern(TestCase):
    """
        Test of the defined pattern

        (	    		#   Start
        (?=.*\d)		#   must contains one digit from 0-9
        (?=.*[a-z])		#   must contains one lowercase characters
        (?=.*[A-Z])		#   must contains one uppercase characters
        (?=.*[@#$%])	#   must contains one special symbols in the list "@#$%"
        .		        #   match anything with previous condition checking
        {6,20}	        #   length at least 6 characters and maximum of 20
        )               #   End
    """

    @staticmethod
    def confirm_password(pattern, password):
        return re.compile(pattern).match(password)

    def test_user_password_check_valid_pattern(self):
        password = "abcC2@!$"

        self.assertTrue(self.confirm_password(PATTERN, password), True)

    def test_user_password_check_invalid_pattern_only_letters(self):
        password = 'abcdefgh'

        self.assertFalse(self.confirm_password(pattern=PATTERN, password=password))

    def test_user_password_check_invalid_pattern_only_numbers(self):
        password = '12345678'

        self.assertFalse(self.confirm_password(pattern=PATTERN, password=password))

    def test_user_password_check_invalid_pattern_without_special_symbols(self):
        password = '123abcDEF'

        self.assertFalse(self.confirm_password(pattern=PATTERN, password=password))

    def test_user_password_check_invalid_pattern_less_than_six_chars(self):
        password = '1aB!'

        self.assertFalse(self.confirm_password(pattern=PATTERN, password=password))


class PasswordResetTests(TestCase):
    def setUp(self):
        url = reverse('password_reset')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')