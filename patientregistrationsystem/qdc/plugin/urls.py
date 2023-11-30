from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from plugin import views

urlpatterns = [
    path("", views.send_to_plugin, name="send-to-plugin"),
    path(
        "get_participants_by_experiment/<int:experiment_id>/",
        views.select_participants,
    ),
]

urlpatterns += staticfiles_urlpatterns()
