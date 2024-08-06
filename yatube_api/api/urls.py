from rest_framework.routers import SimpleRouter

from django.urls import include, path

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router_api_v1 = SimpleRouter()
router_api_v1.register('posts', PostViewSet)
router_api_v1.register('groups', GroupViewSet)
router_api_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router_api_v1.register('follow', FollowViewSet)

urlpatterns = [
    path('v1/', include(router_api_v1.urls)),
]
