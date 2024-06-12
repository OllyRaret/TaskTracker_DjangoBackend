from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import (
    RegisterView, MyTokenObtainPairView,
    TeamViewSet, ProfileViewSet
)
from boards.views import DashboardView
from tasks.views import TaskListView, TaskCalendarView, TaskViewSet

router = DefaultRouter()
router.register('boards', DashboardView, basename='dashboard')
router.register('tasks', TaskListView, basename='task-list')
router.register('calendar', TaskCalendarView, basename='calendar')
router.register(
    r'project/(?P<board_pk>\d+)/board',
    TaskViewSet,
    basename='board-tasks'
)
router.register(
    r'project/(?P<project_pk>\d+)/team',
    TeamViewSet,
    basename='team'
)
router.register('settings', ProfileViewSet, basename='settings')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path(
        'api/login/',
        MyTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
]
