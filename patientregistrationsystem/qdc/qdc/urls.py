import os

from django import get_version
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as authviews
from django.urls import path, re_path, reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve as staticserve

from configuration import views as confviews
from custom_user.forms import CustomPasswordResetForm
from qdc import views as qdcviews

from .forms import PasswordChangeFormCustomized

admin.autodiscover()

urlpatterns = [
    re_path(r"^admin/", admin.site.urls, name="admin"),
    re_path(r"^rosetta/", include("rosetta.urls")),
    re_path(r"^patient/", include("patient.urls")),
    re_path(r"^user/", include("custom_user.urls")),
    re_path(r"^experiment/", include("experiment.urls")),
    re_path(r"^survey/", include("survey.urls")),
    re_path(r"^export/", include("export.urls")),
    re_path(r"^plugin/", include("plugin.urls")),
    re_path(r"^processing/", include("processing.urls")),
    re_path(r"^home/$", qdcviews.contact, name="contact"),
    re_path(r"^home/$", qdcviews.contact, name="home"),
    re_path(r"^links/$", confviews.useful_links_view, name="useful_links"),
    re_path(r"^accounts/login/$", authviews.LoginView.as_view(), name="login"),
    re_path(r"^account/", include("django.contrib.auth.urls")),
    re_path(
        r"^logout/$",
        authviews.logout_then_login,
        {"login_url": "/home/"},
        name="logout",
    ),
    re_path(
        r"^password_change/$",
        authviews.PasswordChangeView.as_view(
            template_name="registration/change_password_custom.html",
            success_url=reverse_lazy("password_changed"),
            form_class=PasswordChangeFormCustomized,
        ),
        name="password_change",
    ),
    re_path(
        r"^password_changed_redirected/$",
        qdcviews.password_changed,
        name="password_changed",
    ),
    re_path(
        r"^password_change/done/$",
        authviews.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    re_path(
        r"^user/password/reset/$",
        authviews.PasswordResetView.as_view(
            success_url="/user/password/reset/done/",
            form_class=CustomPasswordResetForm,
        ),
        name="password_reset",
    ),
    re_path(r"^user/password/reset/done/$", authviews.PasswordResetDoneView.as_view()),
    re_path(
        r"^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$",
        authviews.PasswordResetConfirmView.as_view(success_url="/user/password/done/"),
    ),
    re_path(r"^user/password/done/$", authviews.PasswordResetCompleteView.as_view()),
    re_path(r"^$", qdcviews.contact, name="contact"),
    re_path(
        r"^language/change/(?P<language_code>(?:(?:\w{2})|(?:\w{2}\-\w{2})))/$",
        qdcviews.language_change,
        name="language_change",
    ),
    re_path(r"^i18n/", include("django.conf.urls.i18n")),
    re_path(r"^home/check_upgrade/$", qdcviews.contact, name="check_upgrade"),
    re_path(r"^home/upgrade_nes/$", qdcviews.upgrade_nes, name="upgrade_nes"),
    path("__debug__/", include("debug_toolbar.urls")),
]


# internationalization
js_info_dict = {
    "packages": (
        "patient",
        "experiment",
        "survey",
        "custom_user",
        "export",
        "plugin",
        "site_static",
    ),
}

urlpatterns += [
    re_path(
        r"^jsi18n/$",
        cache_page(86400, cache="redis", key_prefix="jsi18n-%s" % get_version())(
            JavaScriptCatalog.as_view()
        ),
        name="javascript-catalog",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG404:
    urlpatterns += [
        re_path(
            r"^static/(?P<path>.*)$",
            staticserve,
            {"document_root": os.path.join(os.path.dirname(__file__), "static")},
        ),
    ]

handler403 = qdcviews.qdc_permission_denied_view
