# Generated by Django 3.0.5 on 2020-05-14 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choicess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
                ('choice_a', models.CharField(blank=True, max_length=200, null=True)),
                ('choice_b', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
