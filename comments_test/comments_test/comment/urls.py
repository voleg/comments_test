from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()
router.register(r'comment', CommentViewSet)
urlpatterns = router.urls
