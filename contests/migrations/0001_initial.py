# Generated by Django 2.1.2 on 2018-12-12 07:55

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('short_description', models.TextField(help_text='A short description whch describes your contest.', max_length=250, null=True, verbose_name='Short Description')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(help_text='Give a brief or detailed description for your contest')),
                ('eligibility', models.CharField(help_text='What is the eligibility criteria for participants?', max_length=200, null=True)),
                ('rules', models.CharField(help_text='What are the rules that all participants must follow?', max_length=200, null=True)),
                ('prizes', models.CharField(help_text='Mention prizes for diff positions/winners (If any)', max_length=200, null=True)),
                ('contacts', models.EmailField(help_text='Give your email, phone etc. so that people can contact you if they need to', max_length=254, null=True)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('start_time', models.TimeField(null=True, verbose_name='Start Time')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('end_time', models.TimeField(null=True, verbose_name='End Time')),
                ('unique_code', models.CharField(db_index=True, help_text="A unique code for your contest. between 3-15 characters. May contain only                                       lowercase characters and numbers. For example if the question name is 'Sorting Array',                                       you may name the code SORTARR", max_length=15, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('^[0-9a-z]*$', 'The Unique code can contain only small case alphabets and numbers ')], verbose_name='Unique Code')),
                ('is_public', models.BooleanField(default=True, help_text='If you choose to make this non public, please enter a link below that participants will                                  click to register for the contest. It can lead to a form or a website etc. After they complete                                   registration, it is your responsibility to add them in the participants list via                                   the REST API call.', verbose_name='Is this Public?')),
                ('status', models.IntegerField(default=0, help_text='0-Yet to start, 1- live, 2- ended', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('registration_link', models.URLField(blank=True, verbose_name='Registration Link')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='participating_contests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContestLiveSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('timedelta', models.PositiveIntegerField()),
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questions.Submission')),
            ],
        ),
        migrations.CreateModel(
            name='ContestQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contests.Contest')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
            ],
        ),
        migrations.CreateModel(
            name='ContestQuestionTopSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.ContestQuestion')),
                ('contestsubmission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contests.ContestLiveSubmission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('total_time', models.PositiveIntegerField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.Contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='leaderboard',
            unique_together={('contest', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='contestquestiontopsubmission',
            unique_together={('user', 'contest_question')},
        ),
    ]
