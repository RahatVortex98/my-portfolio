from django.contrib import admin
from webapp.models import About
from .models import Certificate, Configuration, Experience, Project  # Import About model from webapp
from django.utils.html import format_html

@admin.register(About)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'email', 'address','image')  # Display key fields in the admin list view
    list_editable = ('title', 'email', 'address','image')
    search_fields = ('title', 'email', 'address')  # Enable search functionality
    list_filter = ('email',)  # Add filtering options





class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ("facebook", "linkedin", "github", "image_preview", "image_header", "resume", "resume_download_link")  
    list_display_links = ("facebook",)  # ✅ Make 'facebook' a clickable link
    list_editable = ("linkedin", "github", "image_header", "resume")  # ✅ Remove 'facebook' from editable

    def image_preview(self, obj):
        if obj.image_header:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />', obj.image_header.url)
        return "No Image"

    image_preview.short_description = "Image Preview"  # Column Name

    def resume_download_link(self, obj):
        if obj.resume:  
            return format_html('<a href="{}" download>Download</a>', obj.resume.url)
        return "No Resume"

    resume_download_link.short_description = "Resume Download"

admin.site.register(Configuration, ConfigurationAdmin)






@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "link","description")
    list_editable = ("name", "icon", "link","description")  # All fields are editable
    list_display_links = None  # Remove clickable links



@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name", "image_certificate") 
    list_editable = ("name", "image_certificate") 
    list_display_links = None  # Remove clickable links




@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("designation", "start_date","end_date","company") 
    list_editable = ("designation", "start_date","end_date","company")  
    list_display_links = None  # Remove clickable links

