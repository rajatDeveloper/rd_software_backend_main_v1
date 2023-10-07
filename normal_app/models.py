from django.db import models


# Create your models here.
class ServiceType(models.TextChoices):
    MOBILE_DEVELOPMENT = "mobile", "Mobile Development"
    WEB_DEVELOPMENT = "web", "Web Development"
    WEB_LANDING_PAGE = "landing", "Web Landing Page"


class ProjectModel(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    cover_image = models.ImageField(upload_to="project_cover/")
    # images =ArrayField(models.ImageField(upload_to='project_images/'), blank=True, null=True , default=list)
    short_des = models.TextField(max_length=120, default="")
    long_des = models.TextField(max_length=250, default="")
    category = models.CharField(
        max_length=10,
        choices=ServiceType.choices,  # Use the .choices property of the TextChoices class
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True)
    phone_number = models.CharField(max_length=14, null=True)
    msg = models.TextField(max_length=200, null=True)

    class Meta:
        verbose_name = "Contact us"
        verbose_name_plural = "Contact us"

    def __str__(self):
        return self.name


class FeedBack(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50, default=" ")
    feedback_des = models.TextField(max_length=200)
    profile_pic = models.ImageField(upload_to="feedback_images/")

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return self.name + " | " + self.position


class Client(models.Model):
    company_name = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to="client_image/")
    short_des = models.TextField(max_length=120, default="")

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clinets"

    def __str__(self):
        return self.company_name
