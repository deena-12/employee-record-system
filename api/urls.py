from django.urls import path
from .views import receive_employee

urlpatterns = [
    path('employee/', receive_employee),
]
