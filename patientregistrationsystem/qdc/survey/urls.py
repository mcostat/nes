from django.urls import path, re_path
from survey import views

urlpatterns = [
    path("list/", views.survey_list, name="survey_list"),
    path("<int:survey_id>/", views.survey_view, name="survey_view"),
    path("new/", views.survey_create, name="survey_create"),
    path("edit/<int:survey_id>/", views.survey_update, name="survey_edit"),
    path(
        "edit/<int:survey_id>/sensitive_questions/",
        views.survey_update_sensitive_questions,
        name="survey_edit_sensitive_questions",
    ),
    re_path(
        r"^update_acquisitiondate/(?P<survey_id>\d+)/",
        views.update_survey_acquisitiondate_view,
        name="update_survey_acquisitiondate",
    ),
]
