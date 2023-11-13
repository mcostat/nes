from modeltranslation.translator import TranslationOptions, translator

from patient.models import (
    AlcoholFrequency,
    AlcoholPeriod,
    AmountCigarettes,
    ClassificationOfDiseases,
    FleshTone,
    Gender,
    MaritalStatus,
    Payment,
    Religion,
    Schooling,
)


class SchoolingTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Schooling, SchoolingTranslationOptions)


class PaymentTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Payment, PaymentTranslationOptions)


class ReligionTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Religion, ReligionTranslationOptions)


class FleshToneTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(FleshTone, FleshToneTranslationOptions)


class MaritalStatusTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(MaritalStatus, MaritalStatusTranslationOptions)


class GenderTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(Gender, GenderTranslationOptions)


class AmountCigarettesTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(AmountCigarettes, AmountCigarettesTranslationOptions)


class AlcoholFrequencyTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(AlcoholFrequency, AlcoholFrequencyTranslationOptions)


class AlcoholPeriodTranslationOptions(TranslationOptions):
    fields = ("name",)


translator.register(AlcoholPeriod, AlcoholPeriodTranslationOptions)


class ClassificationOfDiseasesTranslationOptions(TranslationOptions):
    fields = (
        "description",
        "abbreviated_description",
    )


translator.register(ClassificationOfDiseases, ClassificationOfDiseasesTranslationOptions)
