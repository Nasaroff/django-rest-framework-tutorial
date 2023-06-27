from django.urls import path, include
from rest_framework.routers import DefaultRouter
from server import views

router = DefaultRouter()

router.register(r'user-profiles', views.UserProfileViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
