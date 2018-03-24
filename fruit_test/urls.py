from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from fruit_test import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'fruit', views.FruitViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]