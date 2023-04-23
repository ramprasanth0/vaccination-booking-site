# Generated by Django 3.2.18 on 2023-04-20 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ufirst_name', models.CharField(max_length=50)),
                ('umail', models.EmailField(max_length=50)),
                ('upassword', models.CharField(max_length=50)),
                ('ucontact', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
