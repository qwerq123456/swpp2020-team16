# Generated by Django 3.1.2 on 2020-10-22 06:51

from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.IntegerField(choices=[(1, 'Istj'), (2, 'Istp'), (3, 'Isfj'), (4, 'Isfp'), (5, 'Intf'), (6, 'Intp'), (7, 'Infj'), (8, 'Infp'), (9, 'Estj'), (10, 'Estp'), (11, 'Esfj'), (12, 'Esfp'), (13, 'Entj'), (14, 'Entp'), (15, 'Enfj'), (16, 'Enfp')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(default=None, max_length=21, unique=True)),
                ('email', models.CharField(default=None, max_length=190, null=True, unique=True)),
                ('password', models.TextField(default=None, null=True)),
                ('salt', models.TextField(default=None, null=True)),
                ('role', models.IntegerField(choices=[(1, 'Coder'), (2, 'Manager'), (3, 'Researcher')])),
            ],
            options={
                'db_table': 'user',
                'ordering': ['-pk'],
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager_group', to='group.group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Coder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coder_group', to='group.group')),
                ('style', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.codingstyle')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
