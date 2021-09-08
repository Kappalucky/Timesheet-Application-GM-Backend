"""Core Admin: Details to show in admin page"""

# Python imports
# Django imports
from django.contrib import admin

# 3rd party apps
# Local app imports
from .models import Timesheet
from .forms import TimesheetForm


class Timesheetadmin(admin.ModelAdmin):
    """View details relating to Timesheet objects"""

    form = TimesheetForm
    model = Timesheet
    list_display = ('__str__', 'project', 'project_code',
                    'hours', 'billable', 'billable_rate',)
    list_filter = ('billable', 'project_code', 'date',)
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'first_name',
                'last_name',
                'project',
                'project_code',
                'hours',
                'billable',
                'billable_rate',
                'client',
                'date',
            ),
        }),
    )
    search_fields = ('project', 'project_code',
                     'first_name', 'last_name', 'client',)
    ordering = ('date', 'hours', 'project', 'project_code')


admin.site.register(Timesheet, Timesheetadmin,)
