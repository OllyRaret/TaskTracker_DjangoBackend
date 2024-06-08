from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import RegisterView, MyTokenObtainPairView
from boards.views import DashboardView

router = DefaultRouter()
router.register('dashboard', DashboardView, basename='dashboard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
