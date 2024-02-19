from django.urls import include, path

from . import views
from rest_framework import routers as drf_routers

urlpatterns = [
    path("", views.index, name="index"),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]

drf_router = drf_routers.DefaultRouter()
drf_router.register(r'jobs', views.JobViewSet)
urlpatterns += drf_router.urls
