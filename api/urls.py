from django.urls import path, include
from rest_framework import routers
#from api.views import CheckboxViewSet
from api import views

#router = routers.DefaultRouter()
#router.register('checkbox', CheckboxViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('checkbox_list', views.checkbox_list, name='checkbox_list'),
    path('checkbox_list/<int:pk>', views.checkbox_detail, name='checkbox_list'),
    path('checkbox_created', views.checkbox_created, name='checkbox_created'),
    path('checkbox_update/<int:pk>', views.checkbox_update, name='checkbox_update'),
    path('checkbox_delete/<int:pk>', views.checkbox_delete, name='checkbox_delete'),
]