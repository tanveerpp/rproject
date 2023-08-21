from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.EmpViewset import EmpViewset
router = routers.DefaultRouter()
router.register(r'emps', EmpViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
