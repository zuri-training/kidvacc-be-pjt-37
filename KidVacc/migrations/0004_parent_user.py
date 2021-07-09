# Generated by Django 3.2 on 2021-07-09 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('KidVacc', '0003_auto_20210707_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='auth.user'),
            preserve_default=False,
        ),
    ]
