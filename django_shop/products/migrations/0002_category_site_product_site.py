# Generated by Django 4.0.4 on 2022-06-06 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='sites.site', verbose_name='Сайт'),
        ),
        migrations.AddField(
            model_name='product',
            name='site',
            field=models.ManyToManyField(null=True, related_name='products', to='sites.site', verbose_name='Сайт'),
        ),
    ]