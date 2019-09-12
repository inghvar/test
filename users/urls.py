from django.urls import path

from .views import *


urlpatterns = [
    path('v1/login', login),
    path('v1/user/<int:pk>', UserRetrieveAPIView.as_view()),
    path('v1/create', UserCreateAPIView.as_view()),
    path('v1/users', UserListAPIView.as_view()),
    path('v1/filered-users', UserFilteredListAPIView.as_view()),
]
