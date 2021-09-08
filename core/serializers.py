"""Core Serializers: Functions to change json to python readable format"""

# Python imports
# Django imports
# 3rd party apps
from rest_framework.serializers import ModelSerializer

# Local app imports
from .models import Timesheet


class TimesheetSerializer(ModelSerializer):
    """Serializes Timesheet data"""

    class Meta:
        model = Timesheet
        fields = ('id', 'first_name', 'last_name', 'client', 'project',
                  'project_code', 'hours', 'billable', 'billable_rate', 'date', 'billable_amount')
        read_only_fields = ('created', 'last_updated', 'billable_amount')
