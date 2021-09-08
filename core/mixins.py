"""Core Mixins: Mixin functions for Rest Framework"""

# Python imports
# Django imports
# 3rd party apps
from rest_framework.renderers import BrowsableAPIRenderer

# Local app imports
from .renderers import BrowsableCamelCaseRenderer, CamelCaseRenderer
from .parsers import SnakeCaseParser


class ToCamelCase(BrowsableAPIRenderer):
    renderer_classes = (BrowsableCamelCaseRenderer, CamelCaseRenderer,)


class FromCamelCase:
    parser_classes = (SnakeCaseParser,)
