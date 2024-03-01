# Generated by Django 5.0.2 on 2024-02-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitedTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submissionId', models.CharField(max_length=100)),
                ('respondentId', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField()),
                ('toolName', models.CharField(max_length=100)),
                ('toolUrl', models.URLField(max_length=1000)),
                ('shortDescription', models.CharField()),
                ('review', models.CharField()),
                ('platform', models.CharField(max_length=100)),
                ('lunchDate', models.DateTimeField()),
                ('logoUrl', models.URLField(max_length=1000)),
                ('priceModel', models.CharField(max_length=100)),
                ('selectedTag', models.CharField(max_length=100)),
            ],
        ),
    ]
