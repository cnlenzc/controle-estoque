from django.conf.urls import url, include
from produto import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'produto', views.ProdutoViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
]
