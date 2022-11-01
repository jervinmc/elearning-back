from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

routers=DefaultRouter()
routers.register(r'',views.ClassRoomFilesView)
urlpatterns=[
    path('',include(routers.urls))
]
