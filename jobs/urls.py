from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = 'jobs'

urlpatterns = [

    path('contact/', contact, name='contact'),
    path('about/', about_us, name='about'),
    path('service/', service, name='service'),
    path('job-post/', job_post, name='job-post'),
    path('job-listing/', job_listing, name='job-listing'),
    path('job-single/<int:id>/', job_single, name='job-single'),
    path('search/', SearchView.as_view(), name='search'),
    path('apply/', apply_job, name='apply'),
    path('service/applyjob_list/', ApplicantsListView.as_view(), name='all-applicants'),
    path('service/service-single1.html/', ApplicantsListView.as_view(), name='algorithm-1'),
    path('service/applyjob_location/', ApplicantPerLocationView.as_view(), name='algorithm-location'),
    path('service/service-single2.html/', ApplicantPerLocationView.as_view(), name='algorithm-2'),
    path('service/applyjob_education/', ApplicantPerEducationView.as_view(), name='algorithm-education'),
    path('service/service-single3.html/', ApplicantPerEducationView.as_view(), name='algorithm-3'),
    path('service/applyjob_experience/', ApplicantPerExperienceView.as_view(), name='algorithm-experience'),
    path('service/service-single4.html/', ApplicantPerExperienceView.as_view(), name='algorithm-4'),
    path('service/applyjob_employer/', ApplicantPerEmployerView.as_view(), name='algorithm-employer'),
    path('service/service-single5.html/', ApplicantPerEmployerView.as_view(), name='algorithm-5'),


 
]
