from django.urls import path
from equipment_profiles import views

urlpatterns = [
    path('equipment-profiles/', views.EquipmentProfileList.as_view()),
    path(
        'equipment-profiles/<int:pk>/', views.EquipmentProfileDetail.as_view()
    ),
]
