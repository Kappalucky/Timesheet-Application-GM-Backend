"""Core Urls: API urls"""

# Python imports
# Django imports
from django.urls import path

# 3rd party apps
# Local app imports
from .views import TimesheetList, TimesheetTotalHours, TimesheetTotalBillableAmount

app_name = 'core'

urlpatterns = [
    path('timesheets/', TimesheetList.as_view(),
         name='timesheets_list'),
    path('timesheets/total_hours/', TimesheetTotalHours.as_view(),
         name='timesheets_total_hours'),
    path('timesheets/total_billable_amount/', TimesheetTotalBillableAmount.as_view(),
         name='timesheets_total_billable_amount'),
]
