from django.db import models
from django.db.models import Field

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model
from wagtail.documents import get_document_model


class HomePage(Page):

    #template= "home/home_page.html"

    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body= RichTextField(blank=True)
#just have this if wagtail images used
    image = models.ForeignKey(
        get_image_model(),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    custom_document = models.ForeignKey(
        get_document_model(),

        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('image'),
        FieldPanel('custom_document'),
    ]