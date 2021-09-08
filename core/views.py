"""Core Views: Details on what data to show"""

# Python imports
# Django imports
from django.utils.translation import gettext_lazy as _

# 3rd party apps
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

# Local app imports
from .serializers import TimesheetSerializer
from .models import Timesheet
from .renderers import CamelCaseRenderer
from .parsers import SnakeCaseParser
from .common import import_to_database
from .pagination import PaginationHandlerMixin


class PageNumberPaginationWithCount(PageNumberPagination):
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })


class TimesheetList(APIView, PaginationHandlerMixin):
    """List all timesheets or create a new timesheet"""

    serializer_class = TimesheetSerializer
    pagination_class = PageNumberPaginationWithCount
    renderer_classes = [CamelCaseRenderer]
    parser_classes = [SnakeCaseParser]

    def get(self, request, format=None):
        """Returns timesheet queryset"""

        timesheets = Timesheet.objects.all()

        """
        When this function is called, it will be slow initially (in milliseconds) as it is creating all of the entries before returning the objects.
        As this will only be called once [unless someone decides to delete the database or all the entries in said database]
        the response will be faster (still in milliseconds) since this function will be skipped
        """

        if len(timesheets) == 0:
            import_to_database()
            timesheets = Timesheet.objects.all()

        page = self.paginate_queryset(timesheets)

        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,
                                                                           many=True).data)
        else:
            serializer = self.serializer_class(timesheets, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        """Create timesheet"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimesheetTotalHours(APIView):
    """HTTP get request for total hours of timesheet query"""

    renderer_classes = [CamelCaseRenderer]

    def get(self, request, format=None):
        """Returns total amount of hours across timesheets"""

        total_hours = Timesheet.objects.get_total_hours()

        if total_hours:
            return Response(total_hours, status=status.HTTP_200_OK)
        else:
            return Response('Error: Unable to get total hours', status=status.HTTP_400_BAD_REQUEST)


class TimesheetTotalBillableAmount(APIView):
    """HTTP get request for total billable amount of timesheet query"""

    def get(self, request, format=None):
        """Returns total billable amount across billable timesheets"""

        total_billable_amount = Timesheet.objects.get_total_billable_amount()

        if total_billable_amount:
            return Response(total_billable_amount, status=status.HTTP_200_OK)
        else:
            return Response('Error: Unable to get total billable amount', status=status.HTTP_400_BAD_REQUEST)
