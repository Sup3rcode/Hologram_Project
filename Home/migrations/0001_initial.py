# Generated by Django 5.0.4 on 2024-04-21 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('Articles_img', models.FileField(upload_to='media/Article/image/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': ' Articles ',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('Comment_txt', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='gallery_Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.FileField(upload_to='media/Tourism/gallery_Album/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': ' gallery_Album',
            },
        ),
        migrations.CreateModel(
            name='Holegram_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=200)),
                ('link_codes', models.CharField(max_length=200)),
                ('link_cods', models.CharField(blank=True, max_length=1000, null=True)),
                ('add_datet', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project_Overview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag', models.CharField(max_length=20)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project_Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Role', models.CharField(max_length=200)),
                ('About_the_role', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
