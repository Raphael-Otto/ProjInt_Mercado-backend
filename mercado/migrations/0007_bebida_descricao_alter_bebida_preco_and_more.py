# Generated by Django 4.2.7 on 2023-11-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercado', '0006_bebida_capa'),
    ]

    operations = [
        migrations.AddField(
            model_name='bebida',
            name='descricao',
            field=models.CharField(default=(0, 0), max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bebida',
            name='preco',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='carne',
            name='preco',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='fruta',
            name='preco',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='laticínio',
            name='preco',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='legume',
            name='preco',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='verdura',
            name='preco',
            field=models.IntegerField(max_length=255),
        ),
    ]