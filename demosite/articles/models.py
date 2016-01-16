from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class Article(Page):
    standfirst = RichTextField(blank=True, max_length=350, help_text='To be displayed in the list view')
    body = RichTextField(blank=True, help_text='Full body of the article')

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('standfirst', classname="full")
    ]
