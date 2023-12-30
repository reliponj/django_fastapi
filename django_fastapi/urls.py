from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('admin/base/setting/', views.settings_view),
    path('admin/', admin.site.urls),
]
