# Generated by Django 4.0.4 on 2023-04-22 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0002_boarduser_board_members_boarduser_board_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=128)),
                ('status', models.CharField(choices=[('ON_WORKING', 'On Working'), ('HOLD', 'Hold'), ('OUT_DATE', 'Out Date'), ('DRAFT', 'Draft')], default='ON_WORKING', max_length=128)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='board.board')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]