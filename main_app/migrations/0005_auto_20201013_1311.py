# Generated by Django 3.1.2 on 2020-10-13 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterField(
            model_name='link',
            name='code_snippet',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='github_project',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='planned_date',
            field=models.DateField(null=True, verbose_name='Planned for'),
        ),
        migrations.AlterField(
            model_name='link',
            name='tags',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
