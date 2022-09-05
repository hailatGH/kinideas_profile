from rest_framework.routers import DefaultRouter

from user.views import *

router = DefaultRouter(trailing_slash=False)

router.register(r'user', UserPrivilegeViewset, basename="user")