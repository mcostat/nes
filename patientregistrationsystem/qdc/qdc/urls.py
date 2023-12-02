import os

from configuration import views as confviews
from custom_user.forms import CustomPasswordResetForm
from django import get_version
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as authviews
from django.urls import include, path, re_path, reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve as staticserve
from qdc import views as qdcviews

from .forms import PasswordChangeFormCustomized

admin.autodiscover()

urlpatterns = [
    re_path(r"^admin/", admin.site.urls, name="admin"),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("rosetta/", include("rosetta.urls")),
    path("patient/", include("patient.urls")),
    path("user/", include("custom_user.urls")),
    path("experiment/", include("experiment.urls")),
    path("survey/", include("survey.urls")),
    path("export/", include("export.urls")),
    path("plugin/", include("plugin.urls")),
    path("home/", qdcviews.contact, name="contact"),
    path("home/", qdcviews.contact, name="home"),
    path("links/", confviews.useful_links_view, name="useful_links"),
    path("accounts/login/", authviews.LoginView.as_view(), name="login"),
    path("account/", include("django.contrib.auth.urls")),
    path(
        "logout/",
        authviews.logout_then_login,
        {"login_url": "/home/"},
        name="logout",
    ),
    path(
        "password_change/",
        authviews.PasswordChangeView.as_view(
            template_name="registration/change_password_custom.html",
            success_url=reverse_lazy("password_changed"),
            form_class=PasswordChangeFormCustomized,
        ),
        name="password_change",
    ),
    path(
        "password_changed_redirected/",
        qdcviews.password_changed,
        name="password_changed",
    ),
    path(
        "password_change/done/",
        authviews.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "user/password/reset/",
        authviews.PasswordResetView.as_view(
            success_url="/user/password/reset/done/",
            form_class=CustomPasswordResetForm,
        ),
        name="password_reset",
    ),
    path("user/password/reset/done/", authviews.PasswordResetDoneView.as_view()),
    re_path(
        r"^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$",
        authviews.PasswordResetConfirmView.as_view(success_url="/user/password/done/"),
    ),
    path("user/password/done/", authviews.PasswordResetCompleteView.as_view()),
    path("", qdcviews.contact, name="contact"),
    re_path(
        r"^language/change/(?P<language_code>(?:(?:\w{2})|(?:\w{2}\-\w{2})))/$",
        qdcviews.language_change,
        name="language_change",
    ),
    path("i18n/", include("django.conf.urls.i18n")),
    path("home/check_upgrade/", qdcviews.contact, name="check_upgrade"),
    path("home/upgrade_nes/", qdcviews.upgrade_nes, name="upgrade_nes"),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))


# internationalization
js_info_dict = {
    "packages": (
        "patient",
        "experiment",
        "survey",
        "custom_user",
        "export",
        "plugin",
        "static_data",
    ),
}

urlpatterns += [
    path(
        "jsi18n/",
        cache_page(86400, cache="redis", key_prefix="jsi18n-%s" % get_version())(JavaScriptCatalog.as_view()),
        name="javascript-catalog",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^static/(?P<path>.*)$",
            staticserve,
            {"document_root": os.path.join(os.path.dirname(__file__), "static")},
        ),
    ]

handler403 = qdcviews.qdc_permission_denied_view
