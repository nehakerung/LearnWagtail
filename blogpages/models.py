from django.db import models
from wagtail.images import get_image_model

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel

# Create your models here.
class BlogIndex(Page):
    #A listing page of all child pages of the BlogIndex page

    template = 'blogpages/blog_index_page.html'
    max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = ['blogpages.BlogDetail']

    subtitle = models.CharField(max_length=100, blank=True)
    body = RichTextField(
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['blogpages'] = BlogDetail.objects.live().public()
        return context

from django.core.exceptions import ValidationError
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

class BlogPageTags(TaggedItemBase):
    content_object = ParentalKey(
        'blogpages.BlogDetail',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )

from wagtail.blocks import  TextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail import blocks

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class BlogDetail(Page):
    subtitle = models.CharField(max_length=100, blank=True)
    tags = ClusterTaggableManager(through=BlogPageTags, blank=True)

    body = StreamField([
        ('static_block', blocks.StaticBlock(
            admin_text='Hello world! I am a StaticBlock'
        )),
        # to try
        ('text', TextBlock()),
        # ('carousel', blocks.StreamBlock(
        #     [
        #         ('image', ImageChooserBlock()),
        #         ('quotation', blocks.StructBlock(
        #             [
        #                 ('text', TextBlock()),
        #                 ('author', TextBlock),
        #             ],
        #         )),
        #     ]
        # )),
        #('page_link', blocks.PageChooserBlock()),
        ('page', blocks.PageChooserBlock(
            required=False,
        )),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
        ('author', SnippetChooserBlock('blogpages.Author')),
    ],

        block_counts={
            #'text': {'min_num': 1},
            'image': {'max_num': 1},
        },
        use_json_field=True,
        blank=True,
        null=True,
    )
    parent_page_types = ['blogpages.BlogIndex']
    subpage_pages = []

    image = models.ForeignKey(
        get_image_model(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('tags'),
        FieldPanel('body'),
    ]

    def clean(self):
        super().clean()

        errors = {}

        if 'blog' in self.title.lower():
            errors['title']="Cannot have the word 'Blog'"

        if 'blog' in self.subtitle.lower():
            errors['subtitle']="Subtitle cannot have the word 'Blog'"

        if 'blog' in self.slug.lower():
            errors['slug']="Slug cannot have the word 'Blog'"

        if errors:
            raise ValidationError(errors)

