"""Core Forms: Forms for Core functionality object creation"""

# Python imports
# Django imports
from django.forms import ModelForm

# 3rd party apps
# Local app imports
from .models import Timesheet


class TimesheetForm(ModelForm):
    """Timesheet creation form"""

    class Meta:
        model = Timesheet
        fields = ('date',
                  'client',
                  'project',
                  'project_code',
                  'first_name',
                  'last_name',
                  'hours',
                  'billable',
                  'billable_rate',
                  )
