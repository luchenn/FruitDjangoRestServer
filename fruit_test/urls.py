from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from fruit_test import views
from django.conf.urls.static import static
from django.conf import settings

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'fruit', views.FruitViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)