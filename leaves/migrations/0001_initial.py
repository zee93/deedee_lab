# Generated by Django 2.0.1 on 2018-01-04 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('day', models.DateField(auto_now_add=True, verbose_name='Leave Day Date')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Sick Leave'), (1, 'Emergency Leave')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='leave_days', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]