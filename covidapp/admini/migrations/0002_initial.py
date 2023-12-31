# Generated by Django 4.2.3 on 2023-07-16 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_auth', '0001_initial'),
        ('admini', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receptionniste',
            fields=[
                ('id_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('id_hopital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admini.hopital')),
            ],
        ),
        migrations.CreateModel(
            name='PersonnelMedical',
            fields=[
                ('id_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('id_hopital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admini.hopital')),
            ],
        ),
    ]
