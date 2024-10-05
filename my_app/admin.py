from django.contrib import admin
from django.utils.html import format_html

from .models import About, Contact, News, Partner, Publication, Review, Service, TeamMember


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at', 'updated_at')
    search_fields = ('full_name', 'email')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'view_count', 'created_time', 'updated_time')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'short_description')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'created_at', 'updated_at')
    search_fields = ('name', 'description')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_time', 'updated_time')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_active', 'created_time', 'updated_time')  # Удалены 'service' и 'rating'
    list_filter = ('is_active',)
    search_fields = ('full_name', 'description')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'view_count', 'created_time', 'updated_time')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'created_time', 'updated_time')
    search_fields = ('first_name', 'last_name', 'position')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    fields = ('first_name', 'last_name', 'patronymic', 'position', 'sphere_of_activity', 'education',
              'scientific_degree', 'legal_practice', 'license', 'membership', 'languages', 'image', 'slug')
