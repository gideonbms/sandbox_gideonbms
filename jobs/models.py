from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
#from accounts.models import User

class UserLog(models.Model):
    
    passcode = models.CharField(max_length=50, default='')
    

    def __str__(self):
        return self.passcode

class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=50, default='')
    Email = models.EmailField(blank=True)
    subject = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.Email


JOB_TYPE = (
    ('Part Time', 'Part Time'),
    ('Full Time', 'Full Time'),
    ('Freelance', 'Freelancer'),
)

CATEGORY = (
    ('Retail', 'Retail'),
    ('Banking', 'Banking'),
    ('Security', 'Security'),
    ('Transportation', 'Transportation'),
    ('HR', 'HR'),
    ('Marketing', 'Marketing'),
    ('IT', 'IT'),
)

class JobListing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    employment_status = models.CharField(choices=JOB_TYPE, max_length=10)
    vacancy = models.CharField(max_length=10, null=True)
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
    (40, 'Master Degree'),
    (30, 'Bachelor Degree'),
    (20, 'High School Diploma'),
    (10, 'A Level'),
)

LOCATION_CHOICES = (
    (70, '5 to 10 miles away'),
    (60, '11 to 20 miles away'),
    (50, '21 to 30 miles away'),
    (40, '31 to 40 miles away'),
    (30, '41 to 50 miles away'),
    (20, '51 to  and above miles away'),

)

EXPERIENCE_CHOICES = (
    (60, 'Super experienced 11 years and above'),
    (50, 'Very experienced 9 to 10 years'),
    (40, 'Experienced 6 to 8 years'),
    (30, 'Moderate Experience 3 to 5 years'),
    (20, 'New 1 to 2 years'),
    (10, 'No Experience 0 to 1 year'),

)

NAME_CHOICES = (
    ('E', 'Elly Morrison'),
    ('A', 'Avik Amble'),
    ('B', 'Benson Adebayo'),
)

class ApplyJob(models.Model):
    name = models.CharField(max_length=100, choices=NAME_CHOICES, default='')
    education = models.IntegerField(choices=EDUCATION_CHOICES, default='')
    experience = models.IntegerField(choices=EXPERIENCE_CHOICES, default='')
    location = models.IntegerField(choices=LOCATION_CHOICES, default='')
    bio = models.TextField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, upload_to='uploads/', null=True)
    
    
    def __str__(self):
       return str(self.name)







