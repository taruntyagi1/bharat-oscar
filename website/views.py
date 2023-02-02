from django.shortcuts import render,redirect
from apps.catalogue.models import *

from django import forms

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import TemplateView
# Create your views here.

class homepage(TemplateView):
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        context = super(homepage,self).get_context_data(**kwargs)
        context['header_menu'] = Header_menu.objects.all().order_by('id')
        context['header_logo'] = Header_logo.objects.all().order_by('id')
        context['banner_image'] = BannerImage.objects.all().order_by('id')
        context['our_focus'] = Our_focus.objects.all().order_by('id')
        context['our_vision'] = Our_vision.objects.all()
        context['our_members'] = Our_members.objects.all()
        context['media_center'] = Media_center.objects.all()


        return context

class knowl(TemplateView):
    template_name = 'Knowl.html'

    def get_context_data(self,**kwargs):
        context = super(knowl,self).get_context_data(**kwargs)
        context['header_menu'] = Header_menu.objects.all().order_by('id')
        context['header_logo'] = Header_logo.objects.all().order_by('id')
        context['interview'] = Interviews.objects.all().order_by('id')
        context['education'] = Education.objects.all().order_by('id')

        return context

class About_us(TemplateView):
    template_name = 'AboutUs.html'
    def get_context_data(self,**kwargs):
        context = super(About_us,self).get_context_data(**kwargs)
        context['header_menu'] = Header_menu.objects.all().order_by('id')
        context['header_logo'] = Header_logo.objects.all().order_by('id')
        context['about'] = About.objects.all().order_by('id')
        context['What_we_do'] = what_we_do.objects.all().order_by('id')

        return context

class Press(TemplateView):
    template_name = 'Press-Release.html'
    def get_context_data(self,**kwargs):
        context = super(Press,self).get_context_data(**kwargs)
        context['header_menu'] = Header_menu.objects.all().order_by('id')
        context['header_logo'] = Header_logo.objects.all().order_by('id')
        context['press_image'] = Press_Image.objects.all().order_by('id')
        context['release'] = Press_release.objects.all().order_by('id')
        context['our_members'] = Our_members.objects.all().order_by('id')


        return context


class contact(TemplateView):
    template_name = 'contact_us.html'
    def get_context_data(self,**kwargs):
        context = super(contact,self).get_context_data(**kwargs)
        context['header_menu'] = Header_menu.objects.all().order_by('id')
        context['header_logo'] = Header_logo.objects.all().order_by('id')

        return context


