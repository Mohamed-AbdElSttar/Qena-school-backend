from .api import *
from rest_framework.routers import DefaultRouter
from .views import get_post_group
router = DefaultRouter()
router.register('student', StudentViewset)
router.register('teacher', TeacheViewset)
router.register('course-group', CourseGroupViewset)
router.register('membership', MembershipViewset)
router.register('admins',AdminViewset)
router.register('post',PostViewset)
from django.urls import path
urlpatterns = [
    path('group-post/<int:id>/',get_post_group,name="postgroup")
    ]
urlpatterns += router.urls
