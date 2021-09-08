"""Core Models: Contains database classes and functions"""

# Python imports
from decimal import *

# Django imports
from django.db import models

# 3rd party apps
# Local app imports
from .managers import TimesheetManager


class Timesheet(models.Model):

    """
    Timesheet model
      * First Name
      * Last Name
      * Client
      * Project
      * Project Code
      * Hours
      * Billable
      * Billable Rate
      * Date
    """

    first_name = models.CharField(blank=False, max_length=50,)
    last_name = models.CharField(blank=False, max_length=50,)
    client = models.CharField(blank=False, max_length=100,)
    project = models.CharField(blank=False, max_length=100,)
    project_code = models.CharField(blank=False, max_length=10,)
    hours = models.DecimalField(
        max_digits=5, decimal_places=2, blank=False, null=False,)
    billable = models.BooleanField(default=False)
    billable_rate = models.DecimalField(
        max_digits=6, decimal_places=2, blank=False, null=False,)
    date = models.DateField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(null=True, blank=True,)

    # Custom manager for timesheet manipulation
    objects = TimesheetManager()

    class Meta:
        ordering = ('created', 'billable',)
        verbose_name = 'Timesheet'
        verbose_name_plural = 'Timesheets'

    def __str__(self):
        return '%s %s' % (self.first_name, self.project)

    @property
    def full_name(self):
        """Returns the full name of the timesheet creator"""
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def billable_amount(self):
        """Calculates billable amount if instance is billable, else return 0"""

        if self.billable:
            return (Decimal(self.hours) * Decimal(self.billable_rate))
        else:
            return Decimal(0.00)
