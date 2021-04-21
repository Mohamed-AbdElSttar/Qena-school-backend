from django.urls import path
from .views import login_user,logout_user, RegisterView, UserView
app_name='users'
urlpatterns = [
    path('login',login_user,name="login"),
    path('logout',logout_user,name="logout"),
    path('signup',RegisterView.as_view(),name="register"),
    path('user',UserView.as_view(),name="user"),

]