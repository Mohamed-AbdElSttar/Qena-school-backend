from .api import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', StudentViewset)
router.register('teacher', TeacheViewset)
router.register('course-group', CourseGroupViewset)
router.register('membership', MembershipViewset)
router.register('admins',AdminViewset)
router.register('post',PostViewset)
urlpatterns = router.urls