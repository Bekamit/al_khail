from django.db import models
from django.utils.translation import gettext_lazy as _

from solo.models import SingletonModel


class Header(SingletonModel):
    city = models.CharField(max_length=15)
    all_real_estates = models.CharField(max_length=30)
    place_ad = models.CharField(max_length=30)
    about_us = models.CharField(max_length=30)

    def __str__(self):
        return 'header content'

    class Meta:
        verbose_name = _('Header')
        verbose_name_plural = _('Header static content')


class Body(SingletonModel):
    main = models.CharField(max_length=10)
    search = models.CharField(max_length=10)
    slogan = models.CharField(max_length=50)
    see_real_estates = models.CharField(max_length=30)
    city = models.CharField(max_length=15)
    estate_type = models.CharField(max_length=20)
    popular = models.CharField(max_length=15)
    new_add = models.CharField(max_length=15)
    all = models.CharField(max_length=10)
    show_result = models.CharField(max_length=30)
    we_have = models.CharField(max_length=50)
    benefits = models.CharField(max_length=50)
    wide_selection = models.CharField(max_length=30)
    confidentiality = models.CharField(max_length=30)
    exclusive_offers = models.CharField(max_length=30)
    feedback = models.CharField(max_length=30)
    view_more = models.CharField(max_length=20)
    furnished = models.CharField(max_length=20)
    completion = models.CharField(max_length=15)
    price_at = models.CharField(max_length=15)
    catalog = models.CharField(max_length=30)
    features_and_amenities = models.CharField(max_length=50)
    description = models.CharField(max_length=15)
    similar_properties = models.CharField(max_length=50)
    mission_and_history = models.CharField(max_length=50)
    mission = models.CharField(max_length=20)
    history = models.CharField(max_length=20)
    company = models.CharField(max_length=20)

    def __str__(self):
        return 'body content'

    class Meta:
        verbose_name = _('Body')
        verbose_name_plural = _('Body static content')


class Footer(SingletonModel):
    contact_us = models.CharField(max_length=30)
    cities = models.CharField(max_length=20)
    estate_types = models.CharField(max_length=30)
    pages = models.CharField(max_length=10)

    def __str__(self):
        return 'footer content'

    class Meta:
        verbose_name = _('Footer')
        verbose_name_plural = _('Footer static content')


class Form(SingletonModel):
    contact_us = models.CharField(max_length=30)
    any_question = models.CharField(max_length=50)
    leave_your_contacts = models.CharField(max_length=100)
    submit_application = models.CharField(max_length=50)
    fill_form = models.CharField(max_length=100)
    sell_with_us = models.CharField(max_length=100)
    download_catalog = models.CharField(max_length=50)
    your_name = models.CharField(max_length=15)
    your_email = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    your_city = models.CharField(max_length=15)
    date = models.CharField(max_length=15)
    send = models.CharField(max_length=10)
    close = models.CharField(max_length=10)
    download = models.CharField(max_length=15)
    select_role = models.CharField(max_length=30)
    agent = models.CharField(max_length=30)
    buyer = models.CharField(max_length=30)
    exploring = models.CharField(max_length=30)

    def __str__(self):
        return 'forms content'

    class Meta:
        verbose_name = _('Form')
        verbose_name_plural = _('Forms static content')


class Error404(SingletonModel):
    not_found = models.CharField(max_length=30)
    error_description = models.CharField(max_length=200)

    def __str__(self):
        return 'error 404 content'

    class Meta:
        verbose_name = _('Error 404')
        verbose_name_plural = _('Error static content')


class DefaultValue(SingletonModel):
    default_image = models.ImageField(upload_to='default_image/', verbose_name='default image path')

    def __str__(self):
        return 'default value'

    @staticmethod
    def default_img():
        return DefaultValue.get_solo().default_image

    class Meta:
        verbose_name = _('Default Value')
        verbose_name_plural = _('Default Values')
