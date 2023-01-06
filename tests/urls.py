from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("notifications/", include("df_notifications.drf.urls")),
    path("_nested_admin/", include("nested_admin.urls")),
]
