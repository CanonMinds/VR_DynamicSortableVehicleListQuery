# Generated by Django 3.0.6 on 2020-05-28 04:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='lookup_id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='car',
            name='order',
            field=models.IntegerField(default=100000),
        ),
        migrations.AddField(
            model_name='car',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
