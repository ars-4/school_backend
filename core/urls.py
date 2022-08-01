from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core import auth, views
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()

router.register('types', views.TypeViewSet, basename='types')
router.register('sclasses', views.SClassViewSet, basename='sclasses')
router.register('subjects', views.SubjectViewSet, basename='subjects')

urlpatterns = [
    path('api/', include(router.urls)),

    path('auth/register/', auth.register_user),
    path('auth/login/', auth.login_user),
    path('auth/logout/', auth.logout_user),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/delete/', auth.delete_token),

    path('api/students/', views.get_students),
    path('api/students/<int:pk>/', views.get_student),
    path('api/teachers/', views.get_teachers),
    path('api/teachers/<int:pk>/', views.get_teacher),
    path('api/persons/', views.get_all_users),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
