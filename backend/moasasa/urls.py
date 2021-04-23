from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .api import *
from rest_framework.routers import DefaultRouter
from .views import get_post_group, get_teacher_groups, get_student_mempership, groups_search

router = DefaultRouter()
router.register("student", StudentViewset)
router.register("teacher", TeacheViewset)
router.register("course-group", CourseGroupViewset)
router.register("membership", MembershipViewset)
router.register("admins", AdminViewset)
router.register("post", PostViewset)
urlpatterns = [
    path("group-post/<int:id>/", get_post_group, name="postgroup"),
    path("teacher-groups/<int:id>/", get_teacher_groups, name="teachergroups"),
    path("student-membership/<int:id>/",
         get_student_mempership, name="studentmembership"),
    path("search-groups", groups_search, name="searchgroups"),

]
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
