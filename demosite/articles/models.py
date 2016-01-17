from __future__ import unicode_literals

from django.db import models
from django.db.models import fields
from taggit.managers import TaggableManager
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class ArticlePage(Page):
    standfirst = RichTextField(blank=True, max_length=350, help_text='To be displayed in the list view')
    body = RichTextField(blank=True, help_text='Full body of the article')
    external_ref = fields.URLField(verbose_name='Source URL', blank=True, null=True)
    category = models.ForeignKey('ArticleCategory',
                                 null=True,
                                 blank=False,
                                 on_delete=models.SET_NULL)

    bg_image = models.ForeignKey('wagtailimages.Image',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='+')

    tags = TaggableManager()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('bg_image'),
        FieldPanel('standfirst', classname="full"),
        FieldPanel('external_ref'),
        FieldPanel('category')
    ]


class ArticleCategory(models.Model):
    name = fields.CharField(max_length=50, null=False, blank=False)
    slug = fields.SlugField(auto_created=True)
    ordering = fields.PositiveSmallIntegerField(db_index=True)
