from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("courses/", include("courses.urls")),  # ✅ this works only if courses/urls.py exists
]
