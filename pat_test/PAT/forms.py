
from django import forms
from ajax_select.fields import AutoCompleteSelectField

from .models import Revision


class RevisionForm(forms.ModelForm):

    class Meta:
        model = Revision
        fields = [
            'date',
            'result',
            'test_engineer'
        ]

    tool = AutoCompleteSelectField('Tool', required=True, help_text=None)
