from django.urls import include, path
from rest_framework.routers import SimpleRouter
from ads import views

ad_router = SimpleRouter()
ad_router.register("ads", views.AdViewSet)

urlpatterns = ad_router.urls
