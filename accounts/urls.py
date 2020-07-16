from django.urls import path
from .views import signup, logout_view

app_name = 'accounts'

urlpatterns = [

    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),


]
