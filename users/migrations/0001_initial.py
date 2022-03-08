# Generated by Django 4.0.1 on 2022-02-15 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('profile_image', models.ImageField(default='photos/pattern.jpg', upload_to='photos')),
                ('short_intro', models.CharField(blank=True, max_length=1000, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('social_github', models.CharField(blank=True, max_length=2000, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=2000, null=True)),
                ('social_youtube', models.CharField(blank=True, max_length=2000, null=True)),
                ('social_linkedin', models.CharField(blank=True, max_length=2000, null=True)),
                ('social_website', models.CharField(blank=True, max_length=2000, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
