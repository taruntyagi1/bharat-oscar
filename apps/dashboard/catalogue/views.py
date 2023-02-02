from apps.catalogue.models import *
from apps.dashboard.catalogue.forms import *
from django.urls import reverse_lazy
from django.shortcuts import render,HttpResponseRedirect
from django.db import models
from django.views.generic import ListView,CreateView,UpdateView
from Bharat.message import ERROR_MESSAGES,SUCCESS_MESSAGES
from django.contrib import messages


class header_menu_list(ListView):
    model = Header_menu
    raise_exception = True
    success_url = reverse_lazy('dashboard:header_menu_list')
    paginate_by = 20
    template_name = 'catalogue/header_menu_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:header_menu_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class header_menu_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/header_menu_form.html'
    model = Header_menu
    form_class = header_menu_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:header_menu_list')


class header_menu_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/header_menu_form.html'
    model = Header_menu
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:header_menu_list')



class header_logo_list(ListView):
    model = Header_logo
    raise_exception = True
    success_url = reverse_lazy('dashboard:header_logo_list')
    paginate_by = 20
    template_name = 'catalogue/header_logo_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:header_logo_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class header_logo_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/header_logo_form.html'
    model = Header_logo
    form_class = header_logo_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:header_logo_list')


class header_logo_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/header_logo_form.html'
    model = Header_logo
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:header_logo_list')


class Banner_list_view(ListView):
    model = BannerImage
    raise_exception = True
    success_url = reverse_lazy('dashboard:banner_image_list')
    paginate_by = 20
    template_name = 'catalogue/banner_image_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:banner_image_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class BannerImageCreateView(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/banner_image_form.html'
    model = BannerImage
    form_class = Banner_Image_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:banner_image_list')


class BannerImageUpdateView(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/banner_image_form.html'
    model = BannerImage
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:banner_image_list')



class Press_Image_list(ListView):
    model = Press_Image
    raise_exception = True
    success_url = reverse_lazy('dashboard:press_image_list')
    paginate_by = 20
    template_name = 'catalogue/press_image_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:press_image_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class Press_Image_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/press_image_form.html'
    model = Press_Image
    form_class = Press_Image_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:press_image_list')


class press_image_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/press_image_form.html'
    model = Press_Image
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:press_image_list')




class Press_release_list(ListView):
    model = Press_release
    raise_exception = True
    success_url = reverse_lazy('dashboard:press_release_List')
   
    template_name = 'catalogue/press_release_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:press_release_List')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class Press_release_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/press_release_form.html'
    model = Press_release
    form_class = Press_release_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:press_release_List')


class press_release_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/press_release_form.html'
    model = Press_release
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:press_release_List')



class our_vision_list(ListView):
    model = Our_vision
    raise_exception = True
    success_url = reverse_lazy('dashboard:our_vision_list')
    paginate_by = 20
    template_name = 'catalogue/our_vision_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:our_vision_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class our_vision_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/our_vision_form.html'
    model = Our_vision
    form_class = Our_vision_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:our_vision_list')


class our_vision_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/our_vision_form.html'
    model = Our_vision
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:our_vision_list')



class Our_focus_list(ListView):
    model = Our_focus
    raise_exception = True
    success_url = reverse_lazy('dashboard:our_focus_list')
    paginate_by = 20
    template_name = 'catalogue/our_focus_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:our_focus_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class Our_focus_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/our_focus_form.html'
    model = Our_focus
    form_class = Our_focus_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:our_focus_list')


class Our_focus_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/our_focus_form.html'
    model = Our_focus
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:our_focus_list')




class Our_members_list(ListView):
    model = Our_members
    raise_exception = True
    success_url = reverse_lazy('dashboard:our_member_list')
    paginate_by = 20
    template_name = 'catalogue/our_member_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:our_member_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class Our_members_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/our_members_form.html'
    model = Our_members
    form_class = Our_members_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:our_member_list')


class Our_members_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/our_members_form.html'
    model = Our_members
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:our_member_list')



class Media_center_list(ListView):
    model = Media_center
    raise_exception = True
    success_url = reverse_lazy('dashboard:media_center_list')
    paginate_by = 20
    template_name = 'catalogue/media_center_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:media_center_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class Media_center_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/media_center_form.html'
    model = Media_center
    form_class = Media_center_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:media_center_list')


class Media_center_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/media_center_form.html'
    model = Media_center
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:media_center_list')




class about_list(ListView):
    model = About
    raise_exception = True
    success_url = reverse_lazy('dashboard:about_list')
    paginate_by = 20
    template_name = 'catalogue/about_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:about_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class about_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/about_form.html'
    model = About
    form_class = about_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:about_list')


class about_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/about_form.html'
    model = About
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:about_list')



class what_we_list(ListView):
    model = what_we_do
    raise_exception = True
    success_url = reverse_lazy('dashboard:what_we_list')
    paginate_by = 20
    template_name = 'catalogue/what_we_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:what_we_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class what_we_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/what_we_form.html'
    model = what_we_do
    form_class = what_we_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:what_we_list')


class what_we_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/what_we_form.html'
    model = what_we_do
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:what_we_list')




class interview_list(ListView):
    model = Interviews
    raise_exception = True
    success_url = reverse_lazy('dashboard:interview_list')
    paginate_by = 20
    template_name = 'catalogue/interview_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:interview_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class interview_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/interview_form.html'
    model = Interviews
    form_class = interview_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:interview_list')


class interview_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/interview_form.html'
    model = Interviews
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:interview_list')




class education_list(ListView):
    model = Education
    raise_exception = True
    success_url = reverse_lazy('dashboard:education_list')
    paginate_by = 20
    template_name = 'catalogue/education_list.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:education_list')

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.all()
        queryset = self.model.objects.all().order_by('id')

        if self.request.GET.get('is_active'):
            get_is_active = self.request.GET.get('is_active')
            if get_is_active.isdigit():
                queryset = queryset.filter(is_active=bool(int(get_is_active)))
        return queryset

    def post(self, request, *args, **kwargs):
        delete_item_pk = request.POST.get('image')
        error_status = []
        try:
            obj = self.model.objects.get(id=int(delete_item_pk))
            obj.delete()
        except models.ProtectedError as err:
            reason = ', '.join(['{0}: {1}'.format(err.protected_objects.model.__name__, item) for item in err.protected_objects])
            error_status.append(ERROR_MESSAGES['PROTECTED_ERROR'].format(obj.__class__.__name__, obj, reason))
        except self.models.DoesNotExist:
            pass

        if len(error_status) > 0:
            messages.error(request, '<br/>'.join(error_status))

        messages.success(request, SUCCESS_MESSAGES['OBJECTS_DELETED'].format(1, self.model.__name__))

        return HttpResponseRedirect(self.get_success_url())


class education_create(CreateView):
    """
    Banner Image Create View
    """

    template_name = 'catalogue/education_form.html'
    model = Education
    form_class = education_form

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('dashboard:education_list')


class education_update(UpdateView):
    """
    View for Update Image
    """

    template_name = 'catalogue/education_form.html'
    model = Education
    raise_exception = True
    fields = (
        '__all__'
    )

    success_message = SUCCESS_MESSAGES['BANNER_IMAGE_UPDATE']

    def get_success_url(self):
        return reverse_lazy('dashboard:education_list')
