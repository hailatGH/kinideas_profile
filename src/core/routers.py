from rest_framework.routers import DefaultRouter

from user.views import *

router = DefaultRouter(trailing_slash=False)

router.register(r'users', UserPrivilegeViewset, basename="users")
router.register(r'subscribedUsers', SubscribedUsersViewSet,
                basename="subscribedUsers")
router.register(r'noOfSkips', NoOfSkipsViewSet, basename="noOfSkips")
router.register(r'featureRelease', FeatureReleaseViewSet,
                basename="featureRelease")
