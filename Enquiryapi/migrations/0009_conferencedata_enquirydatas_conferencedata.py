# Generated by Django 4.2.2 on 2023-10-09 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Enquiryapi', '0008_remove_enquirydatas_interesteds_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conferencedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Contact', 'Contact'), ('Convert', 'Convert'), ('Gunk', 'Gunk')], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='enquirydatas',
            name='conferencedata',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Enquiryapi.conferencedata'),
        ),
    ]
