from apps.catalogue.models import *
from django import forms

class header_menu_form(forms.ModelForm):

    class Meta:
        model = Header_menu
        fields = (
            '__all__'
        )


class header_logo_form(forms.ModelForm):

    class Meta:
        model = Header_logo
        fields = (
            '__all__'
        )

class Banner_Image_form(forms.ModelForm):


    class Meta:
        model = BannerImage
        fields = (
        '__all__'
        )


class Press_Image_form(forms.ModelForm):
    class Meta:
        model = Press_Image
        fields = (
            '__all__'
        )


class Press_release_form(forms.ModelForm):

    class Meta:
        model = Press_release
        fields = (
            '__all__'
        )


class Our_vision_form(forms.ModelForm):

    class Meta:
        model = Our_vision
        fields = (
            '__all__'
        )


class Our_focus_form(forms.ModelForm):
    class Meta:
        model = Our_focus
        fields = (
            '__all__'
        )


class Our_members_form(forms.ModelForm):
    class Meta:
        model = Our_members
        fields = (
            '__all__'
        )



class Media_center_form(forms.ModelForm):
    class Meta:
        model  = Media_center
        fields = (
            '__all__'
        )


class interview_form(forms.ModelForm):

    class Meta:
        model = Interviews
        fields = (
            '__all__'
        )


class education_form(forms.ModelForm):

    class Meta:
        model = Education
        fields = (
            '__all__'
        )


class about_form(forms.ModelForm):

    class Meta:
        model = About
        fields =(
            '__all__'
        )


class what_we_form(forms.ModelForm):

    class Meta:
        model = what_we_do
        fields = (
            '__all__'
        )