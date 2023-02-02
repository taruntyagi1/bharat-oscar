from django.db import models


class Header_menu(models.Model):
    menu = models.CharField(max_length=100,blank = True)
    hyperlink = models.CharField(max_length=500,blank=True)
    is_active = models.BooleanField(default=True)






class Header_logo(models.Model):
    logo = models.FileField(upload_to='photo/Header',blank = True)
    hyperlink = models.CharField(max_length=500,blank=True)
    is_active = models.BooleanField(default=True)






class BannerImage(models.Model):
    Banner_image = models.ImageField(upload_to='banner',null = True,blank = True)
    title = models.CharField(max_length=1000, null = True,blank=True)
    button = models.CharField(max_length=100,null = True,blank = True)
    hyperlink = models.CharField(max_length=1000,null =True,blank = True)
    is_active = models.BooleanField(default=True)

    @property
    def sys_id(self):
        return "BI{}".format(str(self.pk + 1000).zfill(6))

    
   

   
class Press_Image(models.Model):
    image = models.FileField(upload_to='photo/Press-image',blank=True)
    is_active = models.BooleanField(default=True)


    @property
    def sys_id(self):
        return "PI{}".format(str(self.pk + 1000).zfill(6))


    

class Press_release(models.Model):
    image = models.FileField(upload_to='photo/Press-release',blank=True)
    title = models.CharField(max_length=1000,blank=True)
    hyperlink = models.CharField(max_length=1000,blank=True)
    is_active = models.BooleanField(default=True)


    @property
    def sys_id(self):
        return "PR{}".format(str(self.pk + 1000).zfill(6))




class Our_vision(models.Model):
    main_heading = models.CharField(max_length=200,null =True,blank = True)
    title = models.CharField(max_length=300, null = True,blank=True)
    description = models.TextField(max_length=10000,blank =True)
    image = models.ImageField(upload_to='our_vision',blank=True)
    button = models.CharField(max_length=300,blank = True)
    hyperlink = models.CharField(max_length=500,blank = True)
    is_active = models.BooleanField(default=True)

    @property
    def sys_id(self):
        return "V{}".format(str(self.pk + 1000).zfill(6))


   


class Our_focus(models.Model):
    image = models.FileField(upload_to='our_focus')
    title = models.CharField(max_length=500,blank=True)
    description = models.TextField(max_length=10000,blank = True)
    is_active = models.BooleanField(default=True)

    @property
    def sys_id(self):
        return "OF{}".format(str(self.pk + 1000).zfill(6))


    


class Our_members(models.Model):
    image = models.FileField(upload_to='our_members')
    is_active = models.BooleanField(default=True)
    @property
    def sys_id(self):
        return "OM{}".format(str(self.pk + 1000).zfill(6))


    

    

class Media_center(models.Model):
    image = models.FileField(upload_to='media_center')
    title = models.CharField(max_length=10000,blank = True)
    hyperlink = models.CharField(max_length=500,blank=True)
    is_active = models.BooleanField(default=True)

    @property
    def sys_id(self):
        return "MD{}".format(str(self.pk + 1000).zfill(6))




class Interviews(models.Model):
    title = models.CharField(max_length=300,blank=True)
    icon = models.FileField(upload_to='interviews',blank=True)
    icon_title = models.CharField(max_length=500,blank = True)
    hyperlink = models.CharField(max_length=600,blank = True)
    is_active = models.BooleanField(default=True)

   




class Education(models.Model):
    image = models.FileField(upload_to='Education',blank = True)
    title = models.CharField(max_length=200,blank = True)
    icon = models.FileField(upload_to='icon/Education',blank =True)
    icon_title = models.CharField(max_length=200,blank = True)
    hyperlink = models.CharField(max_length=500,blank=True)
    is_active = models.BooleanField(default=True)







class About(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=1000,blank = True)
    image = models.FileField(upload_to='about_us',blank=True)
    image_title = models.CharField(max_length=200,blank = True)
    is_active = models.BooleanField(default=True)

 


class what_we_do(models.Model):
    image = models.FileField(upload_to='What_we_do/about_us',blank=True)
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=1000,blank = True)
    is_active = models.BooleanField(default=True)

   
    




from oscar.apps.catalogue.models import *  # noqa isort:skip
