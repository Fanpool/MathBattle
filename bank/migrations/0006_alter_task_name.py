# Generated by Django 4.1 on 2022-08-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0005_alter_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Название'),
        ),
    ]