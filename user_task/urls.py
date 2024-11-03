from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_task import apis

router = DefaultRouter()
router.register(r'tasks', apis.TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
