"""Core Managers: Queryset and managers for manipulating database data"""

# Python imports
# Django imports
from django.db.models import Manager, Sum
from django.db.models.fields import DecimalField
from django.db.models.query import QuerySet

# 3rd party apps
# Local app imports


class TimesheetQuerySet(QuerySet):

    """
    Timesheet queryset
      * is_billable(self)
      * not_billable(self)
      * get_total_hours(self)
      * get_billable_hours(self)
      * get_total_billable_rate(self)
      * get_total_timesheets(self)
    """

    def is_billable(self):
        """Create query with only timesheets where billable = True"""

        return self.filter(billable=True)

    def not_billable(self):
        """Create query with only timesheets where billable = False"""

        return self.filter(billable=False)

    def get_total_hours(self):
        """Adds the sum of 'hours' from all objects in query"""

        return self.aggregate(total_hours=Sum('hours', output_field=DecimalField(max_digits=6, decimal_places=2)))

    def get_total_billable_rate(self):
        """Adds the sum of 'billable_rate' from all objects in query"""

        return self.aggregate(total_rate=Sum('billable_rate', output_field=DecimalField(max_digits=6, decimal_places=2)))

    def get_total_timesheets(self):
        """Adds the sum of all objects in query"""

        return self.all().count()


class TimesheetManager(Manager):

    """
    Timesheet manager
      * get-queryset(self)
      * get_total_timesheets(self)
      * get_total_billable_timesheets(self)
      * def get_projects_by_code(self, project_code)
      * get_timesheet_by_client(self, client)
      * get_timesheet_by_date(self, date)
      * is_billable(self)
      * not_billable(self)
      * get_total_hours(self)
      * get_billable_hours(self)
      * get_total_rate(self)
      * get_total_billable_rate(self)
    """

    def get_queryset(self):
        """Calls queryset class"""

        return TimesheetQuerySet(self.model, using=self._db)

    def get_total_timesheets(self):
        """Returns the total count of all timesheets"""

        return self.all().count()

    def get_total_billable_timesheets(self):
        """Returns the total count of all timesheets from is_billable queryset"""

        return self.get_queryset().is_billable().get_total_timesheets()

    def get_projects_by_code(self, project_code):
        """Create query with only timesheets where project_code is user specified"""

        return self.filter(project_code=project_code)

    def get_timesheet_by_client(self, client):
        """Create query with only timesheets where client is user specified"""

        return self.filter(client=client)

    def get_timesheet_by_date(self, date):
        """Create query with only timesheets where date is user specified"""

        return self.filter(date=date)

    def is_billable(self):
        """Returns queryset of timesheets with billable = True"""

        return self.get_queryset().is_billable()

    def not_billable(self):
        """Returns queryset of timesheets with billable = False"""

        return self.get_queryset().not_billable()

    def get_total_hours(self):
        """Returns sum of all timesheet hours"""

        return self.get_queryset().get_total_hours()

    def get_billable_hours(self):
        """Returns sum of all timesheet hours from is_billable queryset"""

        return self.get_queryset().is_billable().get_total_hours()

    def get_total_rate(self):
        """Returns sum of all timesheet billable rates"""

        return self.get_queryset().get_total_billable_rate()

    def get_total_billable_rate(self):
        """Returns sum of all timesheet billable rates from is_billable queryset"""

        return self.get_queryset().is_billable().get_total_billable_rate()

    def get_total_billable_amount(self):
        """Returns sum of all timesheet billable amounts from is_billable queryset"""

        timesheets = self.get_queryset().is_billable()
        sum = 0

        for timesheet in timesheets:
            sum = sum + timesheet.billable_amount

        return sum
