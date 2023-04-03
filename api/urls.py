from django.urls import path, include
from rest_framework import routers
from api.views import CheckboxViewSet
from api import views

router = routers.DefaultRouter()
router.register('checkbox', CheckboxViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('data', views.DataView.as_view()),
]