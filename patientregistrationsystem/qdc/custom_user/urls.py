from custom_user import views
from django.urls import path

urlpatterns = [
    # Reseracher
    path("list/", views.user_list, name="user_list"),
    path("new/", views.user_create, name="user_new"),
    path("view/<int:user_id>/", views.user_view, name="user_view"),
    path("edit/<int:user_id>/", views.user_update, name="user_edit"),
    # Institution
    path("institution/new/", views.institution_create, name="institution_new"),
    path(
        "institution/<int:institution_id>/",
        views.institution_view,
        name="institution_view",
    ),
    path(
        "institution/edit/<int:institution_id>/",
        views.institution_update,
        name="institution_edit",
    ),
]
