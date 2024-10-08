# Generated by Django 4.2.16 on 2024-10-09 12:14

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogpages', '0006_alter_blogdetail_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetail',
            name='body',
            field=wagtail.fields.StreamField([('page_link', 0), ('image', 1), ('document', 2), ('author_profile', 3)], blank=True, block_lookup={0: ('wagtail.blocks.PageChooserBlock', (), {}), 1: ('wagtail.images.blocks.ImageChooserBlock', (), {}), 2: ('wagtail.documents.blocks.DocumentChooserBlock', (), {}), 3: ('wagtail.snippets.blocks.SnippetChooserBlock', ('blogpages.Author',), {})}, null=True),
        ),
    ]
