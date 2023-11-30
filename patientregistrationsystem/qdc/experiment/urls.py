from django.urls import path, re_path
from experiment import views

urlpatterns = [
    # keyword
    path("keyword/search/", views.keyword_search_ajax, name="keywords_search"),
    path(
        "keyword/new/<int:research_project_id>/<path:keyword_name>/",
        views.keyword_create_ajax,
        name="keyword_new",
    ),
    path(
        "keyword/add/<int:research_project_id>/<int:keyword_id>/",
        views.keyword_add_ajax,
        name="keyword_add",
    ),
    path(
        "keyword/remove/<int:research_project_id>/<int:keyword_id>/",
        views.keyword_remove_ajax,
        name="keyword_remove",
    ),
    # research project
    path(
        "research_project/list/",
        views.research_project_list,
        name="research_project_list",
    ),
    path(
        "research_project/new/",
        views.research_project_create,
        name="research_project_new",
    ),
    path(
        "research_project/<int:research_project_id>/",
        views.research_project_view,
        name="research_project_view",
    ),
    path(
        "research_project/edit/<int:research_project_id>/",
        views.research_project_update,
        name="research_project_edit",
    ),
    # publication
    path("publication/list/", views.publication_list, name="publication_list"),
    path("publication/new/", views.publication_create, name="publication_new"),
    path(
        "publication/<int:publication_id>/",
        views.publication_view,
        name="publication_view",
    ),
    path(
        "publication/edit/<int:publication_id>/",
        views.publication_update,
        name="publication_edit",
    ),
    path(
        "publication/<int:publication_id>/add_experiment/",
        views.publication_add_experiment,
        name="publication_add_experiment",
    ),
    # publication (ajax)
    path(
        "get_experiments_by_research_project/<int:research_project_id>/",
        views.get_experiments_by_research_project,
    ),
    # collaborator
    path(
        "researchers/<int:experiment_id>/new_researcher/",
        views.collaborator_create,
        name="collaborator_new",
    ),
    # experiment
    path(
        "research_project/<int:research_project_id>/new_experiment/",
        views.experiment_create,
        name="experiment_new",
    ),
    path("<int:experiment_id>/", views.experiment_view, name="experiment_view"),
    path(
        "edit/<int:experiment_id>/",
        views.experiment_update,
        name="experiment_edit",
    ),
    re_path(
        r"^experiment_research/change_the_order/(?P<collaborator_position_id>\d+)/(?P<command>\w+)/$",
        views.experiment_research_change_order,
        name="experiment_research_change_order",
    ),
    # export
    path(
        "<int:experiment_id>/export/",
        views.experiment_export,
        name="experiment_export",
    ),
    # import
    path("import/", views.experiment_import, name="experiment_import"),
    path(
        "import/<int:research_project_id>/",
        views.experiment_import,
        name="experiment_import",
    ),
    path("import/results/", views.import_log, name="import_log"),
    # Schedule of sending
    path(
        "schedule_of_sending/<int:experiment_id>/",
        views.experiment_schedule_of_sending,
        name="experiment_schedule_of_sending",
    ),
    path(
        "schedule_of_sending/list/",
        views.schedule_of_sending_list,
        name="schedule_of_sending_list",
    ),
    # group
    path("<int:experiment_id>/group/new/", views.group_create, name="group_new"),
    path("group/<int:group_id>/", views.group_view, name="group_view"),
    path("group/edit/<int:group_id>/", views.group_update, name="group_edit"),
    # equipment
    path(
        "setup/",
        views.setup_menu,
        name="setup_menu",
    ),
    # register manufacturer
    path("manufacturer/list/", views.manufacturer_list, name="manufacturer_list"),
    path("manufacturer/new/", views.manufacturer_create, name="manufacturer_new"),
    path(
        "manufacturer/<int:manufacturer_id>/",
        views.manufacturer_view,
        name="manufacturer_view",
    ),
    path(
        "manufacturer/edit/<int:manufacturer_id>/",
        views.manufacturer_update,
        name="manufacturer_edit",
    ),
    # register amplifier
    path("amplifier/list/", views.amplifier_list, name="amplifier_list"),
    path("amplifier/new/", views.amplifier_create, name="amplifier_new"),
    path(
        "amplifier/<int:amplifier_id>/",
        views.amplifier_view,
        name="amplifier_view",
    ),
    path(
        "amplifier/edit/<int:amplifier_id>/",
        views.amplifier_update,
        name="amplifier_edit",
    ),
    # register eeg solution
    path("eegsolution/list/", views.eegsolution_list, name="eegsolution_list"),
    path("eegsolution/new/", views.eegsolution_create, name="eegsolution_new"),
    path(
        "eegsolution/<int:eegsolution_id>/",
        views.eegsolution_view,
        name="eegsolution_view",
    ),
    path(
        "eegsolution/edit/<int:eegsolution_id>/",
        views.eegsolution_update,
        name="eegsolution_edit",
    ),
    # register filter type
    path("filtertype/list/", views.filtertype_list, name="filtertype_list"),
    path("filtertype/new/", views.filtertype_create, name="filtertype_new"),
    path(
        "filtertype/<int:filtertype_id>/",
        views.filtertype_view,
        name="filtertype_view",
    ),
    path(
        "filtertype/edit/<int:filtertype_id>/",
        views.filtertype_update,
        name="filtertype_edit",
    ),
    # register electrode model
    path("electrodemodel/list/", views.electrodemodel_list, name="electrodemodel_list"),
    path("electrodemodel/new/", views.electrodemodel_create, name="electrodemodel_new"),
    path(
        "electrodemodel/<int:electrodemodel_id>/",
        views.electrodemodel_view,
        name="electrodemodel_view",
    ),
    path(
        "electrodemodel/edit/<int:electrodemodel_id>/",
        views.electrodemodel_update,
        name="electrodemodel_edit",
    ),
    # register material
    path("material/list/", views.material_list, name="material_list"),
    path("material/new/", views.material_create, name="material_new"),
    path("material/<int:material_id>/", views.material_view, name="material_view"),
    path(
        "material/edit/<int:material_id>/",
        views.material_update,
        name="material_edit",
    ),
    # register eeg electrode net
    path(
        "eegelectrodenet/list/",
        views.eegelectrodenet_list,
        name="eegelectrodenet_list",
    ),
    path(
        "eegelectrodenet/new/",
        views.eegelectrodenet_create,
        name="eegelectrodenet_new",
    ),
    path(
        "eegelectrodenet/<int:eegelectrodenet_id>/",
        views.eegelectrodenet_view,
        name="eegelectrodenet_view",
    ),
    path(
        "eegelectrodenet/edit/<int:eegelectrodenet_id>/",
        views.eegelectrodenet_update,
        name="eegelectrodenet_edit",
    ),
    # register cap size
    path(
        "eeg_electrode_cap_size/<int:eegelectrode_cap_id>/add_size/",
        views.eegelectrodenet_cap_size_create,
        name="eegelectrodenet_add_size",
    ),
    path(
        "eeg_electrode_cap_size/<int:eegelectrode_cap_size_id>/",
        views.eegelectrodenet_cap_size_view,
        name="eegelectrodenet_cap_size_view",
    ),
    path(
        "eeg_electrode_cap_size/<int:eegelectrode_cap_size_id>/edit/",
        views.eegelectrodenet_cap_size_update,
        name="eegelectrodenet_cap_size_edit",
    ),
    # register A/D converter
    path("ad_converter/list/", views.ad_converter_list, name="ad_converter_list"),
    path("ad_converter/new/", views.ad_converter_create, name="ad_converter_new"),
    path(
        "ad_converter/<int:ad_converter_id>/",
        views.ad_converter_view,
        name="ad_converter_view",
    ),
    path(
        "ad_converter/edit/<int:ad_converter_id>/",
        views.ad_converter_update,
        name="ad_converter_edit",
    ),
    # register Standardization system (EMG Electrode Placement System)
    path(
        "standardization_system/list/",
        views.standardization_system_list,
        name="standardization_system_list",
    ),
    path(
        "standardization_system/new/",
        views.standardization_system_create,
        name="standardization_system_new",
    ),
    path(
        "standardization_system/<int:standardization_system_id>/",
        views.standardization_system_view,
        name="standardization_system_view",
    ),
    path(
        "standardization_system/edit/<int:standardization_system_id>/",
        views.standardization_system_update,
        name="standardization_system_edit",
    ),
    re_path(
        r"^standardization_system/(?P<standardization_system_id>\d+)/new_placement/(?P<placement_type>\w+)/$",
        views.emg_electrode_placement_create,
        name="emg_electrode_placement_new",
    ),
    path(
        "emg_electrode_placement/<int:emg_electrode_placement_id>/",
        views.emg_electrode_placement_view,
        name="emg_electrode_placement_view",
    ),
    path(
        "emg_electrode_placement/<int:emg_electrode_placement_id>/edit/",
        views.emg_electrode_placement_update,
        name="emg_electrode_placement_edit",
    ),
    # register muscle
    path("muscle/list/", views.muscle_list, name="muscle_list"),
    path("muscle/new/", views.muscle_create, name="muscle_new"),
    path("muscle/<int:muscle_id>/", views.muscle_view, name="muscle_view"),
    path("muscle/edit/<int:muscle_id>/", views.muscle_update, name="muscle_edit"),
    path(
        "muscle/<int:muscle_id>/new_muscle_subdivision/",
        views.muscle_subdivision_create,
        name="muscle_subdivision_new",
    ),
    path(
        "muscle_subdivision/<int:muscle_subdivision_id>/",
        views.muscle_subdivision_view,
        name="muscle_subdivision_view",
    ),
    path(
        "muscle_subdivision/<int:muscle_subdivision_id>/edit/",
        views.muscle_subdivision_update,
        name="muscle_subdivision_edit",
    ),
    path(
        "muscle/<int:muscle_id>/new_muscle_side/",
        views.muscle_side_create,
        name="muscle_side_new",
    ),
    path(
        "muscle_side/<int:muscle_side_id>/",
        views.muscle_side_view,
        name="muscle_side_view",
    ),
    path(
        "muscle_side/<int:muscle_side_id>/edit/",
        views.muscle_side_update,
        name="muscle_side_edit",
    ),
    # source code setting
    path(
        "<int:experiment_id>/source_code/new/",
        views.source_code_create,
        name="source_code_new",
    ),
    path(
        "source_code/<int:source_code_id>/",
        views.source_code_view,
        name="source_code_view",
    ),
    path(
        "source_code/edit/<int:source_code_id>/",
        views.source_code_update,
        name="source_code_edit",
    ),
    # register software
    path("software/list/", views.software_list, name="software_list"),
    path("software/new/", views.software_create, name="software_new"),
    path("software/<int:software_id>/", views.software_view, name="software_view"),
    path(
        "software/edit/<int:software_id>/",
        views.software_update,
        name="software_edit",
    ),
    path(
        "software/<int:software_id>/new_version/",
        views.software_version_create,
        name="software_version_new",
    ),
    path(
        "software_version/<int:software_version_id>/",
        views.software_version_view,
        name="software_version_view",
    ),
    path(
        "software_version/<int:software_version_id>/edit/",
        views.software_version_update,
        name="software_version_edit",
    ),
    # stimuli equipment
    path(
        "<int:experiment_id>/stimuli_eq_setting/new/",
        views.stimuli_eq_setting_create,
        name="stimuli_eq_setting_new",
    ),
    path(
        "stimuli_eq_setting/<int:stimuli_eq_setting_id>/",
        views.stimuli_eq_setting_view,
        name="stimuli_eq_setting_view",
    ),
    path(
        "stimuli_eq_setting/edit/<int:stimuli_eq_setting_id>/",
        views.stimuli_eq_setting_update,
        name="stimuli_eq_setting_edit",
    ),
    path("stimuli_eq/list/", views.stimuli_eq_list, name="stimuli_eq_list"),
    path("stimuli_eq/new/", views.stimuli_eq_create, name="stimuli_eq_new"),
    path(
        "stimuli_eq/<int:stimuli_eq_id>/",
        views.stimuli_eq_view,
        name="stimuli_eq_view",
    ),
    path(
        "stimuli_eq/edit/<int:stimuli_eq_id>/",
        views.stimuli_eq_update,
        name="stimuli_eq_edit",
    ),
    # register EMG electrode placement
    # register coil model
    path("coil/list/", views.coil_list, name="coil_list"),
    path("coil/new/", views.coil_create, name="coil_new"),
    path("coil/<int:coil_id>/", views.coil_view, name="coil_view"),
    path("coil/edit/<int:coil_id>/", views.coil_update, name="coil_edit"),
    # register TMS device
    path("tmsdevice/list/", views.tmsdevice_list, name="tmsdevice_list"),
    path("tmsdevice/new/", views.tmsdevice_create, name="tmsdevice_new"),
    path(
        "tmsdevice/<int:tmsdevice_id>/",
        views.tmsdevice_view,
        name="tmsdevice_view",
    ),
    path(
        "tmsdevice/edit/<int:tmsdevice_id>/",
        views.tmsdevice_update,
        name="tmsdevice_edit",
    ),
    # TMS Localization system and position
    path(
        "tms_localization_system/list/",
        views.tms_localization_system_list,
        name="tms_localization_system_list",
    ),
    path(
        "tms_localization_system/new/",
        views.tms_localization_system_create,
        name="tms_localization_system_new",
    ),
    path(
        "tms_localization_system/<int:tms_localization_system_id>/",
        views.tms_localization_system_view,
        name="tms_localization_system_view",
    ),
    path(
        "tms_localization_system/edit/<int:tms_localization_system_id>/",
        views.tms_localization_system_update,
        name="tms_localization_system_update",
    ),
    path(
        "eeg_electrode_localization_system/list/",
        views.eeg_electrode_localization_system_list,
        name="eeg_electrode_localization_system_list",
    ),
    path(
        "eeg_electrode_localization_system/new/",
        views.eeg_electrode_localization_system_create,
        name="eeg_electrode_localization_system_new",
    ),
    path(
        "eeg_electrode_localization_system/<int:eeg_electrode_localization_system_id>/",
        views.eeg_electrode_localization_system_view,
        name="eeg_electrode_localization_system_view",
    ),
    path(
        "eeg_electrode_localization_system/edit/<int:eeg_electrode_localization_system_id>/",
        views.eeg_electrode_localization_system_update,
        name="eeg_electrode_localization_system_edit",
    ),
    path(
        "eeg_electrode_localization_system/<int:eeg_electrode_localization_system_id>/new_position/",
        views.eeg_electrode_position_create,
        name="eeg_electrode_position_create",
    ),
    path(
        "eeg_electrode_position/<int:eeg_electrode_position_id>/",
        views.eeg_electrode_position_view,
        name="eeg_electrode_position_view",
    ),
    path(
        "eeg_electrode_position/edit/<int:eeg_electrode_position_id>/",
        views.eeg_electrode_position_update,
        name="eeg_electrode_position_edit",
    ),
    path(
        "eeg_electrode_localization_system/<int:eeg_electrode_localization_system_id>/new_coordinates/",
        views.eeg_electrode_coordinates_create,
        name="eeg_electrode_coordinates_create",
    ),
    path(
        "eeg_electrode_localization_system/test/<int:eeg_electrode_localization_system_id>/",
        views.eeg_electrode_localization_system_test,
        name="eeg_electrode_localization_system_test",
    ),
    re_path(
        r"^eeg_electrode_position/change_the_order/(?P<eeg_electrode_position_id>\d+)/(?P<command>\w+)/$",
        views.eeg_electrode_position_change_the_order,
        name="eeg_electrode_position_change_the_order",
    ),
    # eeg setting
    path(
        "<int:experiment_id>/eeg_setting/new/",
        views.eeg_setting_create,
        name="eeg_setting_new",
    ),
    path(
        "eeg_setting/<int:eeg_setting_id>/",
        views.eeg_setting_view,
        name="eeg_setting_view",
    ),
    path(
        "eeg_setting/edit/<int:eeg_setting_id>/",
        views.eeg_setting_update,
        name="eeg_setting_edit",
    ),
    re_path(
        r"^eeg_setting/(?P<eeg_setting_id>\d+)/(?P<eeg_setting_type>\w+)/$",
        views.view_eeg_setting_type,
        name="view_eeg_setting_type",
    ),
    re_path(
        r"^eeg_setting/(?P<eeg_setting_id>\d+)/(?P<eeg_setting_type>\w+)/edit/$",
        views.edit_eeg_setting_type,
        name="edit_eeg_setting_type",
    ),
    path(
        "eeg_setting/eeg_electrode_position_status/<int:eeg_setting_id>/",
        views.eeg_electrode_position_setting,
        name="eeg_electrode_position_setting",
    ),
    path(
        "eeg_setting/eeg_electrode_cap/<int:eeg_setting_id>/",
        views.eeg_electrode_cap_setting,
        name="eeg_electrode_cap_setting",
    ),
    path(
        "eeg_setting/eeg_electrode_position_status/edit/<int:eeg_setting_id>/",
        views.edit_eeg_electrode_position_setting,
        name="edit_eeg_electrode_position_setting",
    ),
    path(
        "eeg_setting/eeg_electrode_position_status_model/<int:eeg_setting_id>/",
        views.eeg_electrode_position_setting_model,
        name="eeg_electrode_position_setting_model",
    ),
    path(
        "eeg_setting/eeg_electrode_position_status_model/edit/<int:eeg_setting_id>/",
        views.edit_eeg_electrode_position_setting_model,
        name="edit_eeg_electrode_position_setting_model",
    ),
    re_path(
        r"^eeg_electrode_position_setting/change_the_order/(?P<eeg_electrode_position_setting_id>\d+)/"
        r"(?P<command>\w+)/$",
        views.eeg_electrode_position_setting_change_the_order,
        name="eeg_electrode_position_setting_change_the_order",
    ),
    # eeg setting (ajax)
    re_path(
        r"^equipment/get_equipment_by_manufacturer/(?P<equipment_type>\w+)/(?P<manufacturer_id>\d+)/$",
        views.get_json_equipment_by_manufacturer,
    ),
    path(
        "equipment/<int:equipment_id>/attributes/",
        views.get_json_equipment_attributes,
    ),
    path(
        "solution/<int:solution_id>/attributes/",
        views.get_json_solution_attributes,
    ),
    path("filter/<int:filter_id>/attributes/", views.get_json_filter_attributes),
    path(
        "equipment/get_localization_system_by_electrode_net/<int:equipment_id>/",
        views.get_localization_system_by_electrode_net,
    ),
    re_path(
        r"^equipment/get_equipment_by_manufacturer_and_localization_system/"
        r"(?P<manufacturer_id>\w+)/(?P<eeg_localization_system_id>\d+)/$",
        views.get_equipment_by_manufacturer_and_localization_system,
    ),
    path(
        "eeg_electrode_localization_system/get_positions/<int:eeg_electrode_localization_system_id>/",
        views.get_json_positions,
    ),
    # emg setting
    path(
        "<int:experiment_id>/emg_setting/new/",
        views.emg_setting_create,
        name="emg_setting_new",
    ),
    path(
        "emg_setting/<int:emg_setting_id>/",
        views.emg_setting_view,
        name="emg_setting_view",
    ),
    path(
        "emg_setting/edit/<int:emg_setting_id>/",
        views.emg_setting_update,
        name="emg_setting_edit",
    ),
    path(
        "emg_setting/<int:emg_setting_id>/digital_filter/",
        views.emg_setting_digital_filter,
        name="emg_setting_digital_filter",
    ),
    path(
        "emg_setting/<int:emg_setting_id>/digital_filter/edit/",
        views.emg_setting_digital_filter_edit,
        name="emg_setting_digital_filter_edit",
    ),
    path(
        "emg_setting/<int:emg_setting_id>/ad_converter/",
        views.emg_setting_ad_converter,
        name="emg_setting_ad_converter",
    ),
    path(
        "emg_setting/<int:emg_setting_id>/ad_converter/edit/",
        views.emg_setting_ad_converter_edit,
        name="emg_setting_ad_converter_edit",
    ),
    path(
        "emg_setting/<int:emg_setting_id>/electrode/add/",
        views.emg_setting_electrode_add,
        name="emg_setting_electrode_add",
    ),
    path(
        "emg_electrode_setting/<int:emg_electrode_setting_id>/",
        views.emg_electrode_setting_view,
        name="emg_electrode_setting_view",
    ),
    path(
        "emg_electrode_setting/<int:emg_electrode_setting_id>/edit/",
        views.emg_electrode_setting_edit,
        name="emg_electrode_setting_edit",
    ),
    path(
        "emg_electrode_setting/<int:emg_electrode_setting_id>/preamplifier/",
        views.emg_electrode_setting_preamplifier,
        name="emg_electrode_setting_preamplifier",
    ),
    path(
        "emg_electrode_setting/<int:emg_electrode_setting_id>/preamplifier/edit/",
        views.emg_electrode_setting_preamplifier_edit,
        name="emg_electrode_setting_preamplifier_edit",
    ),
    path(
        "emg_electrode_setting/<int:emg_electrode_setting_id>/amplifier/",
        views.emg_electrode_setting_amplifier,
        name="emg_electrode_setting_amplifier",
    ),
    path(
        "emg_electrode_setting/<int:emg_electrode_setting_id>/amplifier/edit/",
        views.emg_electrode_setting_amplifier_edit,
        name="emg_electrode_setting_amplifier_edit",
    ),
    # emg setting (ajax)
    path(
        "emg_setting/get_muscle_side_by_electrode_placement/<int:emg_electrode_placement_id>/",
        views.get_json_muscle_side_by_electrode_placement,
    ),
    path(
        "emg_setting/get_electrode_model/<int:electrode_id>/attributes/",
        views.get_json_electrode_model,
    ),
    re_path(
        r"^emg_setting/get_electrode_by_type/(?P<electrode_type>\w+)/$",
        views.get_json_electrode_by_type,
    ),
    re_path(
        r"^emg_setting/get_electrode_placement_by_type/(?P<electrode_type>\w+)/$",
        views.get_electrode_placement_by_type,
    ),
    re_path(
        r"^emg_setting/get_description_by_placement/(?P<emg_electrode_type>\w+)/(?P<emg_electrode_placement_id>\d+)/$",
        views.get_anatomical_description_by_placement,
    ),
    path(
        "coilmodel/<int:coilmodel_id>/attributes/",
        views.get_json_coilmodel_attributes,
    ),
    # tms setting
    path(
        "<int:experiment_id>/tms_setting/new/",
        views.tms_setting_create,
        name="tms_setting_new",
    ),
    path(
        "tms_setting/<int:tms_setting_id>/",
        views.tms_setting_view,
        name="tms_setting_view",
    ),
    path(
        "tms_setting/edit/<int:tms_setting_id>/",
        views.tms_setting_update,
        name="tms_setting_edit",
    ),
    path(
        "tms_setting/<int:tms_setting_id>/tms_device/",
        views.tms_setting_tms_device,
        name="tms_setting_tms_device",
    ),
    path(
        "tms_setting/<int:tms_setting_id>/tms_device/edit/",
        views.tms_setting_tms_device_edit,
        name="tms_setting_tms_device_edit",
    ),
    path(
        "tms_setting/<int:tms_setting_id>/coil_model/",
        views.tms_setting_coil_model,
        name="tms_setting_coil_model",
    ),
    # context tree setting
    path(
        "<int:experiment_id>/context_tree/new/",
        views.context_tree_create,
        name="context_tree_new",
    ),
    path(
        "context_tree/<int:context_tree_id>/",
        views.context_tree_view,
        name="context_tree_view",
    ),
    path(
        "context_tree/edit/<int:context_tree_id>/",
        views.context_tree_update,
        name="context_tree_edit",
    ),
    # cid
    path("group_diseases/cid-10/", views.search_cid10_ajax, name="cid10_search"),
    # classification_of_diseases (add, remove)
    path(
        "group/<int:group_id>/diagnosis/<int:classification_of_diseases_id>/",
        views.classification_of_diseases_insert,
        name="classification_of_diseases_insert",
    ),
    path(
        "diagnosis/delete/<int:group_id>/<int:classification_of_diseases_id>/",
        views.classification_of_diseases_remove,
        name="classification_of_diseases_remove",
    ),
    # subject
    path("group/<int:group_id>/subjects/", views.subjects, name="subjects"),
    path("subject/search/", views.search_patients_ajax, name="subject_search"),
    path(
        "group/<int:group_id>/add_subject/<int:patient_id>/",
        views.subjects_insert,
        name="subject_insert",
    ),
    path(
        "group/<int:group_id>/subject/<int:subject_id>/upload_file/",
        views.upload_file,
        name="upload_file",
    ),
    path(
        "group/<int:group_id>/search_subjects/",
        views.search_subjects,
        name="search_subjects",
    ),
    # subject + questionnaire
    path(
        "group/<int:group_id>/subject/<int:subject_id>/",
        views.subject_questionnaire_view,
        name="subject_questionnaire",
    ),
    re_path(
        r"^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/questionnaire/"
        r"(?P<questionnaire_id>[0-9-]+)/add_response/$",
        views.subject_questionnaire_response_create,
        name="subject_questionnaire_response",
    ),
    re_path(
        r"^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/questionnaire/"
        r"(?P<questionnaire_id>[0-9-]+)/reuse_fill/(?P<patient_questionnaire_response_id>\d+)$",
        views.subject_questionnaire_response_reuse,
        name="subject_questionnaire_response_reuse",
    ),
    path(
        "questionnaire_response/edit/<int:questionnaire_response_id>/",
        views.questionnaire_response_edit,
        name="questionnaire_response_edit",
    ),
    path(
        "questionnaire_response/<int:questionnaire_response_id>/",
        views.questionnaire_response_view,
        name="questionnaire_response_view",
    ),
    # subject + questionnaire data
    path(
        "group/<int:group_id>/load_questionnaire_data/",
        views.load_questionnaire_data,
        name="load_questionnaire_data",
    ),
    # subject + eeg data
    path(
        "group/<int:group_id>/subject/<int:subject_id>/eeg/",
        views.subject_eeg_view,
        name="subject_eeg_view",
    ),
    re_path(
        r"^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/eeg/(?P<eeg_configuration_id>[0-9-]+)/add_eeg_data/$",
        views.subject_eeg_data_create,
        name="subject_eeg_data_create",
    ),
    path(
        "eeg_data/<int:eeg_data_id>/<int:tab>/",
        views.eeg_data_view,
        name="eeg_data_view",
    ),
    path(
        "eeg_data/edit/<int:eeg_data_id>/<int:tab>/",
        views.eeg_data_edit,
        name="eeg_data_edit",
    ),
    path(
        "eeg_data/edit_image/<int:eeg_data_id>/<int:tab>/",
        views.eeg_image_edit,
        name="eeg_image_edit",
    ),
    path(
        "eeg_file/<int:eeg_file_id>/export_nwb/<int:some_number>/<int:process_requisition>/",
        views.eeg_file_export_nwb,
        name="eeg_file_export_nwb",
    ),
    re_path(
        r"^eeg_electrode_position_collection_status/change_the_order/"
        r"(?P<eeg_electrode_position_collection_status_id>\d+)/(?P<command>\w+)/$",
        views.eeg_electrode_position_collection_status_change_the_order,
        name="eeg_electrode_position_collection_status_change_the_order",
    ),
    # eeg_data (ajax)
    path(
        "equipment/get_cap_size_list_from_eeg_setting/<int:eeg_setting_id>/",
        views.get_cap_size_list_from_eeg_setting,
    ),
    path("eeg_data/edit_image/set_worked_positions/", views.set_worked_positions),
    path(
        "eeg_data/get_process_requisition_status/<int:process_requisition>/",
        views.eeg_data_get_process_requisition_status,
    ),
    # subject + emg data
    path(
        "group/<int:group_id>/subject/<int:subject_id>/emg/",
        views.subject_emg_view,
        name="subject_emg_view",
    ),
    re_path(
        r"^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/emg/(?P<emg_configuration_id>[0-9-]+)/add_emg_data/$",
        views.subject_emg_data_create,
        name="subject_emg_data_create",
    ),
    path("emg_data/<int:emg_data_id>/", views.emg_data_view, name="emg_data_view"),
    path(
        "emg_data/edit/<int:emg_data_id>/",
        views.emg_data_edit,
        name="emg_data_edit",
    ),
    # subject + tms_data
    path(
        "group/<int:group_id>/subject/<int:subject_id>/tms/",
        views.subject_tms_view,
        name="subject_tms_view",
    ),
    re_path(
        r"^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/tms/(?P<tms_configuration_id>[0-9-]+)/add_tms_data/$",
        views.subject_tms_data_create,
        name="subject_tms_data_create",
    ),
    path("tms_data/<int:tms_data_id>/", views.tms_data_view, name="tms_data_view"),
    path(
        "tms_data/edit/<int:tms_data_id>/<int:tab>/",
        views.tms_data_edit,
        name="tms_data_edit",
    ),
    path(
        "tms_data/<int:tms_data_id>/position_setting_register/",
        views.tms_data_position_setting_register,
        name="tms_data_position_setting_register",
    ),
    path(
        "tms_data/<int:tms_data_id>/position_setting_view/",
        views.tms_data_position_setting_view,
        name="tms_data_position_setting_view",
    ),
    # data collection
    re_path(
        r"^group/(?P<group_id>\d+)/data_collection_manage/"
        + r"(?P<path_of_configuration>[0-9-]+)/(?P<data_type>\w+)/$",
        views.data_collection_manage,
        name="data_collection_manage",
    ),
    # tms_data(ajax)
    path(
        "get_pulse_by_tms_setting/<int:tms_setting_id>/",
        views.get_pulse_by_tms_setting,
    ),
    # subject + digital_game_phase_data
    path(
        "group/<int:group_id>/subject/<int:subject_id>/digital_game_phase/",
        views.subject_digital_game_phase_view,
        name="subject_digital_game_phase_view",
    ),
    re_path(
        r"^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/digital_game_phase/"
        r"(?P<digital_game_phase_configuration_id>[0-9-]+)/add_digital_game_phase_data/$",
        views.subject_digital_game_phase_data_create,
        name="subject_digital_game_phase_data_create",
    ),
    path(
        "digital_game_phase_data/<int:digital_game_phase_data_id>/",
        views.digital_game_phase_data_view,
        name="digital_game_phase_data_view",
    ),
    path(
        "digital_game_phase_data/edit/<int:digital_game_phase_data_id>/",
        views.digital_game_phase_data_edit,
        name="digital_game_phase_data_edit",
    ),
    # subject + goalkeeper_game_data
    path(
        "group/<int:group_id>/goalkeeper_game_data/",
        views.group_goalkeeper_game_data,
        name="group_goalkeeper_game_data",
    ),
    path(
        "group/<int:group_id>/load_goalkeeper_game_data/",
        views.load_group_goalkeeper_game_data,
        name="load_group_goalkeeper_game_data",
    ),
    # subject + generic_data_collection_data
    path(
        "group/<int:group_id>/subject/<int:subject_id>/generic_data_collection/",
        views.subject_generic_data_collection_view,
        name="subject_generic_data_collection_view",
    ),
    re_path(
        r"^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/generic_data_collection/"
        r"(?P<generic_data_collection_configuration_id>[0-9-]+)/add_generic_data_collection_data/$",
        views.subject_generic_data_collection_data_create,
        name="subject_generic_data_collection_data_create",
    ),
    path(
        "generic_data_collection_data/<int:generic_data_collection_data_id>/",
        views.generic_data_collection_data_view,
        name="generic_data_collection_data_view",
    ),
    path(
        "generic_data_collection_data/edit/<int:generic_data_collection_data_id>/",
        views.generic_data_collection_data_edit,
        name="generic_data_collection_data_edit",
    ),
    # subject + additional data
    path(
        "group/<int:group_id>/subject/<int:subject_id>/additional_data/",
        views.subject_additional_data_view,
        name="subject_additional_data_view",
    ),
    re_path(
        r"^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/additional_data/"
        r"(?P<path_of_configuration>[0-9-]+)/add/$",
        views.subject_additional_data_create,
        name="subject_additional_data_create",
    ),
    path(
        "additional_data/<int:additional_data_id>/",
        views.additional_data_view,
        name="additional_data_view",
    ),
    path(
        "additional_data/edit/<int:additional_data_id>/",
        views.additional_data_edit,
        name="additional_data_edit",
    ),
    re_path(
        r"^group/(?P<group_id>\d+)/subject/(?P<subject_id>\d+)/subject_step_data/"
        r"(?P<path_of_configuration>[0-9-]+)/add/$",
        views.subject_step_data_create,
        name="subject_step_data_create",
    ),
    path(
        "subject_step_data/edit/<int:subject_step_data_id>/",
        views.subject_step_data_edit,
        name="subject_step_data_edit",
    ),
    # experimental protocol components
    path(
        "<int:experiment_id>/components/",
        views.component_list,
        name="component_list",
    ),
    re_path(
        r"^(?P<experiment_id>\d+)/new_component/(?P<component_type>\w+)/$",
        views.component_create,
        name="component_new",
    ),
    re_path(
        r"^component/(?P<path_of_the_components>[0-9-UG]+)/$",
        views.component_view,
        name="component_view",
    ),
    re_path(
        r"^component/edit/(?P<path_of_the_components>[0-9-UG]+)/$",
        views.component_update,
        name="component_edit",
    ),
    re_path(
        r"^component/(?P<path_of_the_components>[0-9-UG]+)/add_new/(?P<component_type>\w+)/$",
        views.component_add_new,
        name="component_add_new",
    ),
    re_path(
        r"^component/(?P<path_of_the_components>[0-9-UG]+)/add/(?P<component_id>\d+)/$",
        views.component_reuse,
        name="component_reuse",
    ),
    re_path(
        r"^component/change_the_order/(?P<path_of_the_components>[0-9-UG]+)/(?P<component_configuration_index>[0-9-]+)/"
        r"(?P<command>\w+)/$",
        views.component_change_the_order,
        name="component_change_the_order",
    ),
    # Questionnaire
    path(
        "group/<int:group_id>/questionnaire/<int:component_configuration_id>/",
        views.questionnaire_view,
        name="questionnaire_view",
    ),
]
