# coding=utf-8
from models import Experiment, QuestionnaireConfiguration
from django.forms import ModelForm, TextInput, Textarea, Select


class ExperimentForm(ModelForm):
    class Meta:
        model = Experiment

        fields = ['title', 'description']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Entrar titulo',
                                      'id': "experiment_title"}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrar descrição',
                                           'rows': '4', 'id': 'experiment_description'}),
        }


class QuestionnaireConfigurationForm(ModelForm):
    class Meta:
        model = QuestionnaireConfiguration
        fields = ['number_of_fills', 'interval_between_fills_value', 'interval_between_fills_unit']

        widgets = {
            'number_of_fills': TextInput(attrs={'class': 'form-control',
                                                'placeholder': '',
                                                'id': "number_of_fills",
                                                'required': "",
                                                'data-error': 'Quantidade deve ser preenchida.'}),
            'interval_between_fills_value': TextInput(attrs={'class': 'form-control',
                                                             'placeholder': '',
                                                             'id': "interval_between_fills_value",
                                                             'required': "",
                                                             'data-error': 'Intervalo deve ser preenchido.'}),
            'interval_between_fills_unit': Select(attrs={'class': 'form-control',
                                                         'id': 'interval_between_fills_unit',
                                                         'required': "",
                                                         'data-error': "Unidade deve ser preenchida"}),
        }
