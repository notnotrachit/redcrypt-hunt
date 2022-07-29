# Generated by Django 4.0.4 on 2022-07-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0005_rename_score_question_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.CharField(max_length=255)),
                ('img_url', models.URLField(blank=True, null=True)),
                ('level', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Sample Questions',
            },
        ),
    ]
