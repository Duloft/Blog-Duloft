# Generated by Django 4.2 on 2023-09-23 16:30

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('complaint_text', ckeditor.fields.RichTextField()),
                ('possible_solution', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Unresolved', 'Unresolved'), ('Closed', 'Closed')], default='Pending', help_text='Stage act which the log is.         Pending is untended to Active is being tended to closed is tended to and resolved Unresolved tended to but not resolved', max_length=20)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_filed', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
