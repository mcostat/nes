from django.urls import path

from .views import (
    experiment_selection,
    export_create,
    export_menu,
    export_view,
    filter_participants,
    search_diagnosis,
    search_locations,
    select_experiments_by_study,
    select_groups_by_experiment,
)

urlpatterns = [
    path("", export_menu, name="export_menu"),
    path("create/", export_create, name="export_create"),
    path("view/", export_view, name="export_view"),
    path("filter_participants/", filter_participants, name="filter_participants"),
    path("experiment_selection/", experiment_selection, name="experiment_selection"),
    # export (ajax)
    path("get_locations/", search_locations, name="search_locations"),
    path("get_diagnosis/", search_diagnosis, name="search_diagnosis"),
    path(
        "get_experiments_by_study/<int:study_id>/",
        select_experiments_by_study,
    ),
    path(
        "get_groups_by_experiment/<int:experiment_id>/",
        select_groups_by_experiment,
    ),
]
