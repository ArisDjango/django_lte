# Generated by Django 4.1.6 on 2023-02-14 08:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_channel_material_unit_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seo_content_overview',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]