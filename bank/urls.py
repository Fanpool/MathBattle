from django.urls import path

from rest_framework.routers import DefaultRouter

from .api import TaskViewSet


urlpatterns = [
]

rounter = DefaultRouter()
rounter.register(r'task', TaskViewSet, basename='task')

urlpatterns += rounter.urls