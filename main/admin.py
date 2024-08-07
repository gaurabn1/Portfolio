from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

@admin.register(ContactProfile)
class  ContactProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'name']

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'score']

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_image']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active']