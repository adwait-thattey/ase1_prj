# Generated by Django 2.1.2 on 2018-10-23 18:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_fail', models.BooleanField(default=False, editable=False, help_text='False means code did not pass the TC.True means it passes')),
            ],
        ),
        migrations.AddField(
            model_name='testcase',
            name='points',
            field=models.PositiveIntegerField(default=0, help_text='The number of points that user will get if he/she completes this                                          test case successfully. The total points lateron will be calculated as a percentage of 100', verbose_name='Points'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submission',
            name='total_score',
            field=models.FloatField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0.0, 'The score can not be negative'), django.core.validators.MaxValueValidator(100.0, 'Total Score must be calculated as a percentage of 100')]),
        ),
        migrations.AddField(
            model_name='result',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Submission'),
        ),
        migrations.AddField(
            model_name='result',
            name='testcase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.TestCase'),
        ),
    ]
