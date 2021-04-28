from django.urls import path
from .views import login_user, logout_user, RegisterView, UserView, register_student, register_teacher, register_admin, \
    check_mail, generate_code_reset_password, check_code_validity, reset_password, confirm_booking_mail

app_name = 'users'
urlpatterns = [
    path('login', login_user, name="login"),
    path('logout', logout_user, name="logout"),
    path('signup', RegisterView.as_view(), name="register"),
    path('user', UserView.as_view(), name="user"),
    path('student-signup', register_student, name="studentsignup"),
    path('teacher-signup', register_teacher, name="teachersignup"),
    path('register_admin', register_admin, name="adminsignup"),
    path("check-mail", check_mail, name="checkmail"),
    path("get-code", generate_code_reset_password, name="getcode"),
    path("check-code", check_code_validity, name="checkcode"),
    path("reset-password", reset_password, name="resetpassword"),
    path("confirm-booking", confirm_booking_mail, name="confirmbooking"),
]
