# Generated by Django 4.2.6 on 2023-10-27 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('mercado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carne',
            name='capa',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
    ]
