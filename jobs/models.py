from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.first_name


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
        
STATUS_CHOICES = (
    ('NEW', 'Entry Level'),
    ('EX', 'Experienced'),
)

PRIORITY_CHOICES = (
    ('I', 'Available Immediately - 2 to 4 weeks'),
    ('N', 'Normal Availability - 1 to 3 Months'),
    ('U', 'Unsure - Undecided'),
)

class ApplyJob(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    web = models.URLField(blank=True)
    entry_status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    availability = models.CharField(max_length=40, choices=PRIORITY_CHOICES, blank=True)
    cv_file = models.FileField(upload_to='uploads/', blank=True)
    resume = models.TextField(blank=True)

    def __str__(self):
       return str(self.id)


