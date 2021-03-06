# Generated by Django 2.1.3 on 2018-11-08 08:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BBS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(blank=True, max_length=256, null=True)),
                ('content', models.TextField()),
                ('view_count', models.IntegerField()),
                ('ranking', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BBS_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(default='This guy is too lazy to levave anything here.', max_length=128)),
                ('user', models.OneToOneField(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('administrator', models.ForeignKey(on_delete=True, to='bbs.BBS_user')),
            ],
        ),
        migrations.AddField(
            model_name='bbs',
            name='author',
            field=models.ForeignKey(on_delete=True, to='bbs.BBS_user'),
        ),
        migrations.AddField(
            model_name='bbs',
            name='category',
            field=models.ForeignKey(on_delete=True, to='bbs.Category'),
        ),
    ]
