from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .api import *
from rest_framework.routers import DefaultRouter

from .views import get_post_group, get_teacher_groups, get_student_mempership, groups_search, get_student_by_user_id, \
    get_teacher_by_user_id, get_admin_by_user_id, today_groups, send_meeting_url, get_membership_by_group, change_to_binding

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

    path("student-membership/<int:id>/", get_student_mempership, name="studentmembership"),
    path('get-user-student/<int:user_id>', get_student_by_user_id, name='get_user_student'),
    path('get-teacher-user/<int:id>',get_teacher_by_user_id,name='get_teacher_by_user_id'),
    path('get-admin-user/<int:user_id>', get_admin_by_user_id, name='get_admin_by_user_id'),
    path("search-groups", groups_search, name="searchgroups"),
    path("today-groups", today_groups, name="todaygroups"),
    path("send-urls", send_meeting_url, name="sendurls"),
    path("get-mems/<int:id>/", get_membership_by_group, name="getmems"),
    path("group-memberships/<int:id>/", change_to_binding, name="change_to_binding"),


]
urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
