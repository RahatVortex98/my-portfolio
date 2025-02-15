from django.urls import path
from .views import HomePageTemplateView, contact_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name="HomePageTemplateView"),  
    path("contact/", contact_view, name="contact"),
]  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
