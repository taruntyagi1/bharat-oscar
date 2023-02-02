from website.views import *
from django.urls import path


urlpatterns = [
    path('',homepage.as_view(),name='homepage'),
    path('knowl/',knowl.as_view(),name='knowl'),
    path('about_us/',About_us.as_view(),name='about_us'),
    path('press/',Press.as_view(),name='press'),
    path('contact_us',contact.as_view(),name='contact_us')
]
