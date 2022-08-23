# Generated by Django 4.1 on 2022-08-23 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_alter_task_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='task',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bank.section', verbose_name='Section'),
        ),
    ]