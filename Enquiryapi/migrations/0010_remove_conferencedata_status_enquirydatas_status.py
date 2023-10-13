# Generated by Django 4.2.2 on 2023-10-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enquiryapi', '0009_conferencedata_enquirydatas_conferencedata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conferencedata',
            name='status',
        ),
        migrations.AddField(
            model_name='enquirydatas',
            name='status',
            field=models.CharField(choices=[('Contact', 'Contact'), ('Convert', 'Convert'), ('Gunk', 'Gunk')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
