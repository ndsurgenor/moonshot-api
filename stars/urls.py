from django.urls import path
from stars import views

urlpatterns = [
    path('stars/', views.StarList.as_view()),
]