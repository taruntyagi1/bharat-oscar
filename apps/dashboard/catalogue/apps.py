import oscar.apps.dashboard.catalogue.apps as apps
from oscar.core.loading import get_class
from django.conf.urls import url



class CatalogueDashboardConfig(apps.CatalogueDashboardConfig):
    name = 'apps.dashboard.catalogue'


    def ready(self):
        super(CatalogueDashboardConfig,self).ready()
        from apps.dashboard.catalogue.views import (
            Banner_list_view,
            BannerImageCreateView,
            BannerImageUpdateView,
            Press_Image_list,
            press_image_update,Press_Image_create,
            Press_release_list,
            Press_release_create,
            press_release_update,
            our_vision_list,
            our_vision_create,
            our_vision_update,
            header_menu_list,
            header_menu_create,
            header_menu_update,
            header_logo_list,
            header_logo_create,
            header_logo_update,
            about_list,
            about_create,
            about_update,
            what_we_list,
            what_we_create,
            what_we_update,
            interview_list,
            interview_create,
            interview_update,
            education_list,education_create,education_update,
            Our_focus_list,Our_focus_create,Our_focus_update,
            Our_members_list,Our_members_create,Our_members_update,
            Media_center_list,Media_center_create,Media_center_update

        )
        self.banner_list = Banner_list_view
        self.banner_create = BannerImageCreateView
        self.banner_update = BannerImageUpdateView
        self.press_image_list =  Press_Image_list
        self.press_image_create = Press_Image_create
        self.press_image_update = press_image_update
        self.press_release_List = Press_release_list
        self.press_release_Create = Press_release_create
        self.press_release_Update = press_release_update
        self.our_vision_list = our_vision_list
        self.our_vision_create = our_vision_create
        self.our_vision_update = our_vision_update
        self.header_menu_list = header_menu_list
        self.header_menu_create = header_menu_create
        self.header_menu_update = header_menu_update
        self.header_logo_list = header_logo_list
        self.header_logo_create = header_logo_create
        self.header_logo_update = header_logo_update
        self.about_list = about_list
        self.about_create = about_create
        self.about_update = about_update
        self.what_we_list = what_we_list
        self.what_we_create = what_we_create
        self.what_we_update = what_we_update
        self.interview_list = interview_list
        self.interview_create = interview_create
        self.interview_update = interview_update
        self.education_list = education_list
        self.education_create = education_create
        self.education_update = education_update
        self.our_focus_list = Our_focus_list
        self.our_focus_create = Our_focus_create
        self.our_focus_update = Our_focus_update
        self.our_member_list = Our_members_list
        self.our_member_create = Our_members_create
        self.our_member_update = Our_members_update
        self.media_list = Media_center_list
        self.media_create = Media_center_create
        self.media_update = Media_center_update



    def get_urls(self):
        urls = super(CatalogueDashboardConfig,self).get_urls()

        urls += [
            url(r'^banner_image/$', self.banner_list.as_view(), name='banner_image_list'),
            url(r'^banner_image/create/$', self.banner_create.as_view(), name='banner_image_create'),
            url(r'^banner_image/(?P<pk>\d+)/update/$', self.banner_update.as_view(), name='banner_image_update'),
            url(r'^press_image/$', self.press_image_list.as_view(), name='press_image_list'),
            url(r'^press_image/create/$', self.press_image_create.as_view(), name='press_image_create'),
            url(r'^press_image/(?P<pk>\d+)/update/$', self.press_image_update.as_view(), name='press_image_update'),
            url(r'^press_release/$', self.press_release_List.as_view(), name='press_release_List'),
            url(r'^press_release/create/$', self.press_release_Create.as_view(), name='press_release_Create'),
            url(r'^press_release/(?P<pk>\d+)/update/$', self.press_release_Update.as_view(), name='press_release_Update'),
            url(r'^our_vision/$', self.our_vision_list.as_view(), name='our_vision_list'),
            url(r'^our_vision/create/$', self.our_vision_create.as_view(), name='our_vision_create'),
            url(r'^our_vision/(?P<pk>\d+)/update/$', self.our_vision_update.as_view(), name='our_vision_update'),
            url(r'^header_menu/$', self.header_menu_list.as_view(), name='header_menu_list'),
            url(r'^header_menu/create/$', self.header_menu_create.as_view(), name='header_menu_create'),
            url(r'^header_menu/(?P<pk>\d+)/update/$', self.header_menu_update.as_view(), name='header_menu_update'),
            url(r'^header_logo/$', self.header_logo_list.as_view(), name='header_logo_list'),
            url(r'^header_logo/create/$', self.header_logo_create.as_view(), name='header_logo_create'),
            url(r'^header_logo/(?P<pk>\d+)/update/$', self.header_logo_update.as_view(), name='header_logo_update'),
            url(r'^our_focus/$', self.our_focus_list.as_view(), name='our_focus_list'),
            url(r'^our_focus/create/$', self.our_focus_create.as_view(), name='our_focus_create'),
            url(r'^our_focus/(?P<pk>\d+)/update/$', self.our_focus_update.as_view(), name='our_focus_update'),
            url(r'^our_member/$', self.our_member_list.as_view(), name='our_member_list'),
            url(r'^our_member/create/$', self.our_member_create.as_view(), name='our_member_create'),
            url(r'^our_member/(?P<pk>\d+)/update/$', self.our_member_update.as_view(), name='our_member_update'),
            url(r'^about/$', self.about_list.as_view(), name='about_list'),
            url(r'^about/create/$', self.about_create.as_view(), name='about_create'),
            url(r'^about/(?P<pk>\d+)/update/$', self.about_update.as_view(), name='about_update'),
            url(r'^what_we/$', self.what_we_list.as_view(), name='what_we_list'),
            url(r'^what_we/create/$', self.what_we_create.as_view(), name='what_we_create'),
            url(r'^what_we/(?P<pk>\d+)/update/$', self.what_we_update.as_view(), name='what_we_update'),
            url(r'^interview/$', self.interview_list.as_view(), name='interview_list'),
            url(r'^interview/create/$', self.interview_create.as_view(), name='interview_create'),
            url(r'^interview/(?P<pk>\d+)/update/$', self.interview_update.as_view(), name='interview_update'),
            url(r'^education/$', self.education_list.as_view(), name='education_list'),
            url(r'^education/create/$', self.education_create.as_view(), name='education_create'),
            url(r'^education/(?P<pk>\d+)/update/$', self.education_update.as_view(), name='education_update'),
            url(r'^media_center/$', self.media_list.as_view(), name='media_center_list'),
            url(r'^media_center/create/$', self.media_create.as_view(), name='media_center_create'),
            url(r'^media_center/(?P<pk>\d+)/update/$', self.media_update.as_view(), name='media_center_update'),



        ]
        return self.post_process_urls(urls)

