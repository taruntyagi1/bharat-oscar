"""
Django settings for Bharat project.

Generated by 'django-admin startproject' using Django 4.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from oscar.defaults import *
import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6@(c8v#h&xu^wfrvn1($qi3cy-7mrqg4vw)6fdjkics@d(@u8p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'website',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'oscar.config.Shop',
    'oscar.apps.analytics.apps.AnalyticsConfig',
    'oscar.apps.checkout.apps.CheckoutConfig',
    'oscar.apps.address.apps.AddressConfig',
    'oscar.apps.shipping.apps.ShippingConfig',
    'apps.catalogue.apps.CatalogueConfig',
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    'oscar.apps.partner.apps.PartnerConfig',
    'oscar.apps.basket.apps.BasketConfig',
    'oscar.apps.payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    'oscar.apps.order.apps.OrderConfig',
    'oscar.apps.customer.apps.CustomerConfig',
    'oscar.apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    'oscar.apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig',

    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',   # Default thumbnail backend, can be replaced
    'django_tables2',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]


OSCAR_DASHBOARD_NAVIGATION = [
    {
        'label': _('Header'),
        'children': [
            {
                'label': _('Header Logo'),
                'url_name': 'dashboard:header_logo_list',
            },
            {
                'label': _('Header Menu'),
                'url_name': 'dashboard:header_menu_list',
            },


        ]
    },
    {
        'label': _('Banner Image'),
        'url_name': 'dashboard:banner_image_list'
    },
    {
        'label': _('Our vision'),
        'url_name': 'dashboard:our_vision_list'
    },
    {
        'label': _('Our focus'),
        'url_name': 'dashboard:our_focus_list'
    },
    {
        'label': _('Our members'),
        'url_name': 'dashboard:our_member_list'
    },
    {
        'label': _('Media center'),
        'url_name': 'dashboard:media_center_list'
    },
    {
        'label': _('Interviews'),
        'url_name': 'dashboard:interview_list'
    },
    {
        'label': _('Education'),
        'url_name': 'dashboard:education_list'
    },
    {
        'label': _('About us'),
        'children': [
            {
                'label': _('About'),
                'url_name': 'dashboard:about_list'
            },
            {
                'label': _('What we do'),
                'url_name': 'dashboard:what_we_list'
            },
        ]
    },
    {
        'label': _('Press release'),
        'children': [
            {
                'label': _('Press release image'),
                'url_name': 'dashboard:press_image_list'
            },
            {
                'label': _('Press Release'),
                'url_name': 'dashboard:press_release_List'
            },
        ]
    },




    # {
    #     'label': _('Our vision'),
    #     'url_name': 'dashboard: our_vision_list'
    # },
    # {
    #     'label': _('Our focus'),
    #     'url_name': 'dashboard: our_focus_list'
    # },
    # {
    #     'label': _('Our members'),
    #     'url_name': 'dashboard: our_members_list'
    # },
    # {
    #     'label': _('Media Center'),
    #     'url_name': 'dashboard: media_center_list'
    # },
    # {
    #     'label': _('Interviews'),
    #     'url_name': 'dashboard: interview_list'
    # },
    # {
    #     'label': _('Education'),
    #     'url_name': 'dashboard: education_list'
    # },
    # {
    #     'label': _('About us'),
    #     'children': [
    #         {

    #             'label': _('About'),
    #             'url_name': 'dashboard: about_list'

    #         },
    #         {

    #             'label': _('What we do'),
    #             'url_name': 'dashboard: what_we_list'

    #         },

    #     ]
    # },
    # {

    #     'label': _('Press release'),
    #     'children' : [
    #         {

    #             'label': _('press release image'),
    #             'url_name': 'dashboard: press_image_list'

    #         },
    #         {

    #             'label': _('press release'),
    #             'url_name': 'dashboard: press_release_list'

    #         },
    #     ]

    # },
]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

ROOT_URLCONF = 'Bharat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'Bharat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'BHARAT',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'ATOMIC_REQUEST': True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'