# Generated by Django 5.0.4 on 2024-04-21 22:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='add_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_add_Article', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='Articles_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Articles_Articles', to='Home.articles'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_add_Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='holegram_video',
            name='add_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_add', to=settings.AUTH_USER_MODEL),
        ),
    ]
