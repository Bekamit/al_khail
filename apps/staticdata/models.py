from django.db import models
from solo.models import SingletonModel


class Header(SingletonModel):
    buy = models.CharField(max_length=10)
    all_properties = models.CharField(max_length=20)
    place_ad = models.CharField(max_length=30)
    contact_as = models.CharField(max_length=30)
    slogan = models.CharField(max_length=50)
    search = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    estate_type = models.CharField(max_length=20)
    show_result = models.CharField(max_length=30)
    filter = models.CharField(max_length=15)
    all = models.CharField(max_length=10)
    popular = models.CharField(max_length=15)
    new_add = models.CharField(max_length=15)

    def __str__(self):
        return 'header'

    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Header static content'


class Body(SingletonModel):
    property = models.CharField(max_length=15)
    about_company = models.CharField(max_length=50)
    why = models.CharField(max_length=10)
    advantages = models.CharField(max_length=30)
    all_properties = models.CharField(max_length=20)
    view_more = models.CharField(max_length=20)
    listing_details = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    price = models.CharField(max_length=15)
    furnished = models.CharField(max_length=20)
    completion = models.CharField(max_length=15)
    estate_type = models.CharField(max_length=20)
    facilities = models.CharField(max_length=50)
    expand_all_photos = models.CharField(max_length=30)
    download_catalog = models.CharField(max_length=30)
    description = models.CharField(max_length=15)
    you_might_like = models.CharField(max_length=50)

    def __str__(self):
        return 'body'

    class Meta:
        verbose_name = 'Body'
        verbose_name_plural = 'Body static content'


class Footer(SingletonModel):
    ...

    def __str__(self):
        return 'footer'

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer static content'


class Form(SingletonModel):
    callback_form_title = models.CharField(max_length=50)
    sell_form_title = models.CharField(max_length=50)
    download_catalog_form_title = models.CharField(max_length=50)
    form_description = models.CharField(max_length=100)
    sell_form_description = models.CharField(max_length=100)
    your_name = models.CharField(max_length=15)
    your_email = models.CharField(max_length=15)
    your_phone = models.CharField(max_length=15)
    your_city = models.CharField(max_length=15)
    at_date = models.CharField(max_length=15)
    send = models.CharField(max_length=10)
    role = models.CharField(max_length=30)
    agent = models.CharField(max_length=30)
    buyer = models.CharField(max_length=30)
    exploring = models.CharField(max_length=30)
    download = models.CharField(max_length=15)

    def __str__(self):
        return 'form'

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms static content'


class DefaultValue(SingletonModel):
    default_image = models.ImageField(upload_to='default_image/', verbose_name='default image path')

    def __str__(self):
        return 'default value'

    @staticmethod
    def default_img():
        return DefaultValue.objects.first().default_image

    class Meta:
        verbose_name = 'Default Value'
        verbose_name_plural = 'Default Values'
