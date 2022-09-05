from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from user.serializers import *
from .models import *

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class UserPrivilegeViewset(viewsets.ModelViewSet):

    queryset = UserPrivilegeModel.objects.all()
    serializer_class = UserPrivilegeSerializer
    pagination_class = StandardResultsSetPagination