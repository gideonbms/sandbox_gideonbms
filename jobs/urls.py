from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = 'jobs'

urlpatterns = [

    path('contact/', contact, name='contact'),
    path('experiment/', about_us, name='experiment'),
    path('service/', service, name='service'),
    path('job-post/', job_post, name='job-post'),
    path('job-listing/', job_listing, name='job-listing'),
    path('job-single/<int:id>/', job_single, name='job-single'),
    path('search/', SearchView.as_view(), name='search'),
    path('apply/', apply_job, name='apply'),
    path('service/applyjob_list/', ApplicantsListView.as_view(), name='all-applicants'),
      
]
