from django.urls import path
from user_profiles import views

urlpatterns = [
    path('user-profiles/', views.UserProfileList.as_view()),
]