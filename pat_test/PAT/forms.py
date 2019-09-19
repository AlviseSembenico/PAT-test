
from django import forms
from ajax_select import make_ajax_field
from django.conf import settings

from .models import Revision


class RevisionForm(forms.ModelForm):

    class Meta:
        model = Revision
        fields = '__all__'

    tool = make_ajax_field(Revision, 'tool', 'Tool', help_text=None)
    field_order = ['tool', 'date', 'test_engineer', 'result']
    date =  forms.DateField(
        widget=forms.DateInput(format=settings.DATE_INPUT_FORMATS[0]),
        input_formats=settings.DATE_INPUT_FORMATS
        )
    result = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=[
            (1, 'Pass'),
            (2, 'Fail')
        ],
    )
    visual_check = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=[
            (1, 'Pass'),
            (2, 'Fail')
        ],
    )
    function_check = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=[
            (1, 'Pass'),
            (2, 'Fail')
        ],
    )
