from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from rest_framework.routers import DefaultRouter


from .comment.urls import router as comment_router


router = DefaultRouter()
router.registry = (
    comment_router.registry
)
api_calls = router.urls


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_calls, namespace='api')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^storage/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    ]
