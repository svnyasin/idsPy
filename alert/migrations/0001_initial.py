# Generated by Django 4.0.3 on 2022-03-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapturedPackets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_content', models.TextField(verbose_name='captured_packets')),
            ],
        ),
    ]
