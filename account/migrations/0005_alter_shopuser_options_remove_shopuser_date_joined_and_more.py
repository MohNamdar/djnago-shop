# Generated by Django 5.1.1 on 2024-09-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_shopuser_date_joined'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopuser',
            options={'verbose_name': 'کاربر', 'verbose_name_plural': 'کاربران'},
        ),
        migrations.RemoveField(
            model_name='shopuser',
            name='date_joined',
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='address',
            field=models.CharField(max_length=255, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='first_name',
            field=models.CharField(max_length=25, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='کارمند'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='last_name',
            field=models.CharField(max_length=25, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='phone',
            field=models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن'),
        ),
    ]
