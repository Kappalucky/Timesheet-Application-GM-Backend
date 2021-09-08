"""Core Parsers: Changes the formatting of variables"""

# Python imports
# Django imports
# 3rd party apps
from rest_framework.parsers import JSONParser

# Local app imports
from .common import deep_snake_case_transform


class SnakeCaseParser(JSONParser):
    def parse(self, stream, *args, **kwargs):
        data = super().parse(stream, *args, **kwargs)
        return deep_snake_case_transform(data)
