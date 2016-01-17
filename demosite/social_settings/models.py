from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    email = models.EmailField(
        help_text='Contact email address')
    github = models.CharField(
        max_length=255, help_text='Github username')
    linkedin = models.URLField(
        help_text='linkedIn profile URL')