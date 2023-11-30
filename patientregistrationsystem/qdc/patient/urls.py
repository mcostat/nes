from django.urls import path
from patient import views

urlpatterns = [
    path("", views.search_patient, name="search_patient"),
    path("find/", views.search_patient, name="search_patient"),
    path("advanced_search/", views.advanced_search, name="advanced_search"),
    path("new/", views.patient_create, name="patient_new"),
    path("edit/<int:patient_id>/", views.patient_update, name="patient_edit"),
    path("search/", views.search_patients_ajax, name="patient_search"),
    path(
        "verify_homonym/",
        views.patients_verify_homonym,
        name="patients_verify_homonym",
    ),
    path(
        "verify_homonym_excluded/",
        views.patients_verify_homonym_excluded,
        name="patients_verify_homonym_excluded",
    ),
    path("<int:patient_id>/", views.patient_view, name="patient_view"),
    path("restore/<int:patient_id>/", views.restore_patient, name="patient_restore"),
    # medical_record (create, read, update)
    path(
        "<int:patient_id>/medical_record/new/",
        views.medical_record_create,
        name="medical_record_new",
    ),
    path(
        "<int:patient_id>/medical_record/<int:record_id>/",
        views.medical_record_view,
        name="medical_record_view",
    ),
    path(
        "<int:patient_id>/medical_record/edit/<int:record_id>/",
        views.medical_record_update,
        name="medical_record_edit",
    ),
    # cid
    path("medical_record/cid-10/", views.search_cid10_ajax, name="cid10_search"),
    # diagnosis (create, delete, update)
    path(
        "<int:patient_id>/medical_record/<int:medical_record_id>/diagnosis/<int:cid10_id>/",
        views.diagnosis_create,
        name="diagnosis_create",
    ),
    path(
        "<int:patient_id>/medical_record/new/diagnosis/<int:cid10_id>/",
        views.medical_record_create_diagnosis_create,
        name="medical_record_diagnosis_create",
    ),
    path(
        "diagnosis/delete/<int:patient_id>/<int:diagnosis_id>/",
        views.diagnosis_delete,
        name="diagnosis_delete",
    ),
    # exam (create, read, update, delete)
    path(
        "<int:patient_id>/medical_record/edit/<int:record_id>/diagnosis/<int:diagnosis_id>/exam/new/",
        views.exam_create,
        name="exam_create",
    ),
    path(
        "<int:patient_id>/medical_record/<int:record_id>/exam/<int:exam_id>/",
        views.exam_view,
        name="exam_view",
    ),
    path(
        "<int:patient_id>/medical_record/edit/<int:record_id>/exam/edit/<int:exam_id>/",
        views.exam_edit,
        name="exam_edit",
    ),
    path(
        "<int:patient_id>/medical_record/edit/<int:record_id>/exam/remove/<int:exam_id>/",
        views.exam_delete,
        name="exam_delete",
    ),
    # exam file (delete)
    path(
        "exam_file/delete/<int:exam_file_id>/",
        views.exam_file_delete,
        name="exam_file_delete",
    ),
    # questionnaire response
    path(
        "<int:patient_id>/questionnaire/<int:survey_id>/add_response/",
        views.questionnaire_response_create,
        name="questionnaire_response_create",
    ),
    path(
        "questionnaire_response/<int:questionnaire_response_id>/",
        views.questionnaire_response_view,
        name="questionnaire_response_view",
    ),
    path(
        "questionnaire_response/edit/<int:questionnaire_response_id>/",
        views.questionnaire_response_update,
        name="questionnaire_response_edit",
    ),
]
