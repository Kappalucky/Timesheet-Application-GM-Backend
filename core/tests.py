"""Core Tests: Functions to ensure inner functions of models work correctly"""

# Python imports
from decimal import Decimal

# Django imports
from django.test import TestCase

# 3rd party apps
# Local app imports
from .models import Timesheet


class TimesheetTests(TestCase):
    """Test module for Timesheet model"""

    def setUp(self):
        Timesheet.objects.create(
            first_name="Craig",
            last_name="Brown",
            client="Badman Entities",
            project="Kartel Party",
            project_code="BM004",
            hours="34.02",
            billable="False",
            billable_rate="12.23",
            date="2020-04-21"
        )
        Timesheet.objects.create(
            first_name="Trippie",
            last_name="Redd",
            client="1400/999",
            project="Love Scars",
            project_code="TR666",
            hours="102.00",
            billable="True",
            billable_rate="14.00",
            date="2020-04-21"
        )

    def test_timesheet_created(self):
        billable = Timesheet.objects.get(client="1400/999")
        not_billable = Timesheet.objects.get(project="Kartel Party")

        self.assertTrue(hasattr(billable, "__str__"))
        self.assertTrue(hasattr(not_billable, "__str__"))

    def test_timesheet_str(self):
        billable = Timesheet.objects.get(client="1400/999")
        not_billable = Timesheet.objects.get(project="Kartel Party")

        self.assertEqual(str(billable), '%s %s' %
                         (billable.first_name, billable.project))
        self.assertEqual(str(not_billable), '%s %s' %
                         (not_billable.first_name, not_billable.project))

    def test_timesheet_get_fullname(self):
        billable = Timesheet.objects.get(client="1400/999")
        not_billable = Timesheet.objects.get(project="Kartel Party")

        self.assertEqual('%s %s' %
                         (billable.first_name, billable.last_name), billable.full_name)

        self.assertEqual('%s %s' %
                         (not_billable.first_name, not_billable.last_name), not_billable.full_name)

    def test_timesheet_billable_amount_correct(self):
        billable = Timesheet.objects.get(client="1400/999")

        total_billable = float(billable.hours) * float(billable.billable_rate)
        self.assertEqual(total_billable, billable.billable_amount)
