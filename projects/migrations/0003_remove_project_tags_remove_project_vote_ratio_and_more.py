# Generated by Django 4.2.4 on 2023-08-16 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vote_ratio',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vote_total',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
