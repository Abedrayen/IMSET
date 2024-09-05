# Generated by Django 4.2.16 on 2024-09-05 04:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diplomas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diploma',
            old_name='issue_date',
            new_name='graduation_date',
        ),
        migrations.AddField(
            model_name='diploma',
            name='issuance_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diploma',
            name='diploma_type',
            field=models.CharField(choices=[('BTP', 'BTP'), ('BTS', 'BTS')], max_length=3),
        ),
    ]
