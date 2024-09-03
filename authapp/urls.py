from django.urls import path
from .views import UserRegistration,UserLogin,UserLogout

urlpatterns = [
    path('add-user/',UserRegistration.as_view(),name='register_user'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('logout/', UserLogout, name='logout')
]
