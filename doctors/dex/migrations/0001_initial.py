# Generated by Django 3.1.1 on 2020-10-25 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='spex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spex_name', models.CharField(max_length=30)),
                ('spex_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='dox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dox_name', models.CharField(max_length=30)),
                ('dox_spex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dex.spex')),
            ],
        ),
    ]
