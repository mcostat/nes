from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from simple_history.admin import SimpleHistoryAdmin

from .models import (
    AlcoholFrequency,
    AlcoholPeriod,
    AmountCigarettes,
    ClassificationOfDiseases,
    FleshTone,
    Gender,
    MaritalStatus,
    Patient,
    Payment,
    Religion,
    Schooling,
    SocialDemographicData,
    SocialHistoryData,
)

# Register your models here.
search_fields = ["cpf"]

# Register models for Admin history and audit changes
admin.site.register(Patient, SimpleHistoryAdmin)
admin.site.register(SocialDemographicData, SimpleHistoryAdmin)
admin.site.register(SocialHistoryData, SimpleHistoryAdmin)


@admin.register(Schooling)
class SchoolingAdmin(TranslationAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(TranslationAdmin):
    pass


@admin.register(Religion)
class ReligionAdmin(TranslationAdmin):
    pass


@admin.register(FleshTone)
class FleshToneAdmin(TranslationAdmin):
    pass


@admin.register(MaritalStatus)
class MaritalStatusAdmin(TranslationAdmin):
    pass


@admin.register(Gender)
class GenderAdmin(TranslationAdmin):
    pass


@admin.register(AmountCigarettes)
class AmountCigarettesAdmin(TranslationAdmin):
    pass


@admin.register(AlcoholFrequency)
class AlcoholFrequencyAdmin(TranslationAdmin):
    pass


@admin.register(AlcoholPeriod)
class AlcoholPeriodAdmin(TranslationAdmin):
    pass


@admin.register(ClassificationOfDiseases)
class ClassificationOfDiseasesAdmin(TranslationAdmin):
    pass
