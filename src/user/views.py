from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *

from user.serializers import *
from .models import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class UserPrivilegeViewset(viewsets.ModelViewSet):

    queryset = UserPrivilegeModel.objects.all()
    serializer_class = UserPrivilegeSerializer
    pagination_class = StandardResultsSetPagination


class SubscribedUsersViewSet(viewsets.ModelViewSet):

    queryset = SubscribedUsersModel.objects.all()
    serializer_class = SubscribedUsersSerializer
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        if request.data['subscription_type'] == "MONTHLY":
            date = datetime.now()
            new_paid_until_monthly = date + relativedelta(months=+1)

            pay_load = {}
            pay_load = {
                "user_id": request.data['user_id'],
                "subscription_type": "MONTHLY",
                "subscription_expiry_date": new_paid_until_monthly

            }
        elif request.data['subscription_type'] == "YEARLY":
            date = datetime.now()
            new_paid_until_yearly = date + relativedelta(months=+12)

            pay_load = {}
            pay_load = {
                "user_id": request.data['user_id'],
                "subscription_type": "YEARLY",
                "subscription_expiry_date": new_paid_until_yearly

            }

        serializer = self.serializer_class(
            data=pay_load)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NoOfSkipsViewSet(viewsets.ModelViewSet):

    queryset = NoOfSkipsModel.objects.all()
    serializer_class = NoOfSkipsSerializer
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        return Response("Method not allowed")

    def update(self, request, *args, **kwargs):
        userId = kwargs['pk']

        if not self.queryset.filter(user_id=userId).exists():
            return super().create(request, *args, **kwargs)

        userData = self.queryset.filter(user_id=userId).values(
            'user_id', 'noOfSkips', 'created_at', 'updated_at')
        today = str(date.today())
        lastUpdateDate = str(userData[0]['updated_at'])[:len(today)]

        if lastUpdateDate != today:
            userData.update(noOfSkips=0)

        currentNoOfSkips = userData[0]['noOfSkips']
        noOfSkips = currentNoOfSkips + 1
        userData.update(noOfSkips=noOfSkips)
        userData = self.queryset.filter(user_id=userId).values()
        return Response(userData)
