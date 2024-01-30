from django.urls import path
from stars import views

urlpatterns = [
    path('stars/', views.StarList.as_view()),
    path('stars/<int:pk>/', views.StarDetail.as_view()),
]