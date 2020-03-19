from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
#from accounts.models import User




class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    Email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.Email


JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelancer'),
)

CATEGORY = (
    ('Web Design', 'Web Design'),
    ('Graphic Design', 'Graphic Design'),
    ('Web Developing', 'Web Developing'),
    ('Software Engineering', 'Software Engineering'),
    ('HR', 'HR'),
    ('Marketing', 'Marketing'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Any', 'Any'),
)


class JobListing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    employment_status = models.CharField(choices=JOB_TYPE, max_length=10)
    vacancy = models.CharField(max_length=10, null=True)
    gender = models.CharField(choices=GENDER, max_length=30, null=True)
    category = models.CharField(choices=CATEGORY, max_length =30)
    description = models.TextField()
    responsibilities = models.TextField()
    experience = models.CharField(max_length=100)
    job_location = models.CharField(max_length=120)
    Salary = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='media', null=True)
    application_deadline = models.DateTimeField()
    published_on = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:job-single", args=[self.id])
        
EDUCATION_CHOICES = (
    (1, 'PhD'),
    (2, 'Master Degree'),
    (3, 'Bachelor Degree'),
    (4, 'Undergraduate'),
)

LOCATION_CHOICES = (
    (1, '5 to 99 miles away'),
    (2, '100 to 299 miles away'),
    (3, '300 to 399 miles away'),
    (4, '400 to 499 miles away'),
    (5, '500 to 599 miles away'),
    (6, '600 to 999 miles away'),
    (7, '1000 and above miles away'),
)

EXPERIENCE_CHOICES = (
    (1, 'Super experienced 11 years and above'),
    (2, 'Very experienced 9 to 10 years'),
    (3, 'Experienced 6 to 8 years'),
    (4, 'Moderate Experience 3 to 5 years'),
    (5, 'New 1 to 2 years'),
    (6, 'No Experience 0 to 1 year'),

)

class ApplyJob(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    web = models.URLField(blank=True)
    education = models.IntegerField(choices=EDUCATION_CHOICES, default='')
    experience = models.IntegerField(choices=EXPERIENCE_CHOICES, default='')
    location = models.IntegerField(choices=LOCATION_CHOICES, default='')
    cv_file = models.FileField(upload_to='uploads/', blank=True)
    resume = models.TextField(blank=True)

    def __str__(self):
       return str(self.last_name)


