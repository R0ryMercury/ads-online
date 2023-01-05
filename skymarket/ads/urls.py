from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from ads import views

ads_router = SimpleRouter()
ads_router.register("ads", views.AdViewSet, basename="ads")

comments_router = NestedSimpleRouter(ads_router, "ads", lookup="ad")
comments_router.register("comments", views.CommentViewSet, basename="comments")

urlpatterns = ads_router.urls + comments_router.urls
