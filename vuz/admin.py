from django.contrib import admin
from .models import University, Faculty

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'first', 'second', 'city', 'army')
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'point', 'places', 'price', 'university')
admin.site.register(University, UniversityAdmin)
admin.site.register(Faculty, FacultyAdmin)