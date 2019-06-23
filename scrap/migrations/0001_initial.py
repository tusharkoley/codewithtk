# Generated by Django 2.1.3 on 2019-02-14 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_url', models.CharField(max_length=200)),
                ('search_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl_no', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('paragraph', models.CharField(max_length=2000)),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrap.Index')),
            ],
        ),
    ]
