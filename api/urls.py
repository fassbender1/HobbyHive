from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


app_name = 'api'


router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'events', EventViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'hobbies', HobbyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]