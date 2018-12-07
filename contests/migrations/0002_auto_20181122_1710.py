# Generated by Django 2.1.2 on 2018-11-22 11:40

import ckeditor.fields
import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='contacts',
            field=ckeditor.fields.RichTextField(help_text='Give your email, phone etc. so that people can contact you if they need to', null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Hello', help_text='Give a brief or detailed description for your contest'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contest',
            name='eligibility',
            field=ckeditor.fields.RichTextField(help_text='What is the eligibility criteria for participants?', null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 22, 11, 40, 10, 701332, tzinfo=utc), verbose_name='End Date Time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contest',
            name='is_public',
            field=models.BooleanField(default=True, help_text='If you choose to make this non public, please enter a link below that participants will                                  click to register for the contest. It can lead to a form or a website etc. After they complete                                   registration, it is your responsibility to add them in the participants list via                                   the REST API call', verbose_name='Is this Public?'),
        ),
        migrations.AddField(
            model_name='contest',
            name='participants',
            field=models.ManyToManyField(related_name='participating_contests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contest',
            name='prizes',
            field=ckeditor.fields.RichTextField(help_text='Mention prizes for diff positions/winners (If any)', null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='registration_link',
            field=models.URLField(blank=True, verbose_name='Registration Link'),
        ),
        migrations.AddField(
            model_name='contest',
            name='rules',
            field=ckeditor.fields.RichTextField(help_text='What are the rules that all participants must follow?', null=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date Time'),
            preserve_default=False,
        ),
    ]
