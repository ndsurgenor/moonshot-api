from django.urls import path
from photos import views

urlpatterns = [
    path('photos/', views.PhotoList.as_view()),
    path('photos/<int:pk>/', views.PhotoDetail.as_view()),
]
