
from django import forms
from ajax_select.fields import AutoCompleteSelectField

from .models import Revision


class RevisionForm(forms.ModelForm):

    class Meta:
        model = Revision
        fields = [
            'date',
            'test_engineer',
            'result',
        ]

    tool = AutoCompleteSelectField('Tool', required=True, help_text=None)
    field_order = ['tool', 'date', 'test_engineer', 'result']
