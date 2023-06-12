from django.contrib import admin
from myapp.models import Experience, UserProfile, Education

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'organisation_profile', 'location', 'description']
    #ordering = ('name')
    #search_fields = ('name', 'blood_group', 'address')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'organisation', 'course_details']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']