# Generated by Django 3.1.2 on 2020-10-30 15:39

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_auto_20201030_1539'),
        ('group', '0003_group_name'),
        ('user', '0002_auto_20201030_1539'),
        ('analysis', '0002_report_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UM', models.FloatField()),
                ('TI', models.FloatField()),
                ('EF', models.FloatField()),
                ('JC', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GlobalReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.researcher')),
                ('distribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.distribution')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.researcher')),
                ('distribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.distribution')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProblemReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.researcher')),
                ('distribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analysis.distribution')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.problem')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SolutionReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.researcher')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem.solution')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
