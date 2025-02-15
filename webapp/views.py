from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from .models import About, Certificate, Configuration, Experience, Project,ContactMessage

class HomePageTemplateView(TemplateView):
    template_name = "index.html"

    def get_about_obj(self, *args, **kwargs):
        return About.objects.first()  # Calling the method correctly
    
    def get_configuration_obj(self, *args, **kwargs):
        return Configuration.objects.first()
    
    def get_project_obj(self, *args, **kwargs):
        return Project.objects.first()
    
    def get_certificate_obj(self,*args,**kwargs):
        return Certificate.objects.first()



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_obj'] = self.get_about_obj()  #  Calling the function properly
        context['configuration_obj'] = self.get_configuration_obj()
        context['project_obj'] = Project.objects.all()[:3]
        context['certificate_obj'] = Certificate.objects.all()[:10]
        context['experiences'] = Experience.objects.all().order_by("-start_date")

        return context  
    


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send email
            send_mail(
                subject=f"New Contact Form Submission: {contact.subject}",
                message=f"From: {contact.name} <{contact.email}>\n\n{contact.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],  # Send email to yourself
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")  # Redirect to the same page after submission
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
