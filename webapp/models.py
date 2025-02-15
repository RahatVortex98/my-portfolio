from django.db import models

class About(models.Model):
    heading = models.TextField(
        "About Heading",
         blank=False,null=False
    )
    title = models.CharField(
        "About title",
        max_length=255,blank=False,null=False
    )
    description = models.TextField(
        "About Desc.",
        blank=False,null=False

    )
    email=models.EmailField(
        "About Email",
        max_length=255,
        blank=False,null=False
    )
    image=models.ImageField(
        "About Image",
        upload_to="about_images/",blank=False,null=False
        )
    address=models.TextField(
        "About Address",
        blank=False,null=False
    )
    
    def __str__(self):
        return self.title
    




class Configuration(models.Model): 
    facebook = models.URLField("Facebook", blank=True, null=True)
    linkedin = models.URLField("LinkedIn", blank=True, null=True)
    github = models.URLField("GitHub", blank=True, null=True)
    
    image_header = models.ImageField(
        "Configuration Image",
        upload_to="configuration_images/",
        blank=True,  # Now optional
        null=True
    )

    favicon = models.ImageField(  
        "Favicon",
        upload_to="favicons/",  
        blank=True,  
        null=True
    )

    resume = models.FileField(  
        "Resume PDF",
        upload_to="resumes/",  
        blank=True,  
        null=True
    )

    def __str__(self):
        return f"Configuration: {self.id}"




class Project(models.Model):
    name = models.CharField(
        "Project Name",
        max_length=255)
    description = models.TextField(
        "Project Desc."
    )
    icon = models.CharField(
        "Project Icon",
        max_length=100, help_text="FontAwesome icon class, e.g., 'fa fa-shopping-cart'")
    link = models.URLField(
        "Project link"
    )

    def __str__(self):
        return self.name
    


class Certificate(models.Model):
    name = models.CharField(
        "Course Name",
        max_length=255)
    image_certificate = models.ImageField(
        "Course Certificate",
        upload_to="certificates/")

    def __str__(self):
        return self.name

class Experience(models.Model):
    designation = models.CharField(
        "Designation",
        max_length=255

    )
    start_date = models.DateField()  # e.g., 2024-01-01
    end_date = models.DateField()

    company = models.CharField(
        "Company Name",
        max_length=255

    )

    def __str__(self):
        return self.company
    
    def get_duration(self):
        if self.end_date:
            return f"{self.start_date.strftime('%b %Y')} - {self.end_date.strftime('%b %Y')}"
        return f"{self.start_date.strftime('%b %Y')} - Present"  # Handles ongoing jobs







class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
