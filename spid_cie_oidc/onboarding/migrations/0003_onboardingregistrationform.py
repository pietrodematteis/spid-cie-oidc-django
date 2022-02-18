# Generated by Django 4.0.2 on 2022-02-18 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_onboarding', '0002_alter_federationentityprofile_trust_mark_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnboardingRegistrationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization Name', models.CharField(max_length=100)),
                ('url of the entity', models.CharField(max_length=200)),
                ('url of the page where the SPID/CIE button is available', models.CharField(max_length=200)),
                ('public jwks of the entities', models.CharField(max_length=10000)),
            ],
        ),
    ]
