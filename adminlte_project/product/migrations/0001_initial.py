# Generated by Django 4.1.6 on 2023-02-07 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/category')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=200, null=True, unique=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='featured_image_path')),
                ('bom_file', models.FileField(blank=True, null=True, upload_to='file')),
                ('cost_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DI', 'Disable'), ('EN', 'Enable')], default='EN', max_length=2)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands_product', to='product.brand')),
                ('category', models.ManyToManyField(blank=True, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='AmbienceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='ambience_image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ambience_image', to='product.product')),
            ],
        ),
    ]
