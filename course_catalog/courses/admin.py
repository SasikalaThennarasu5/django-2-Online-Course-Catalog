from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "level")
    list_filter = ("level",)
    search_fields = ("title",)
