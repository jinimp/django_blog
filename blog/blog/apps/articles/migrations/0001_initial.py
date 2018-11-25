# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-30 09:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='更新时间')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('body', mdeditor.fields.MDTextField(verbose_name='内容')),
                ('abstract', models.TextField(blank=True, verbose_name='摘要')),
                ('page_view', models.IntegerField(default=0, verbose_name='浏览量')),
                ('article_image', models.ImageField(null=True, upload_to='', verbose_name='文章图片')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否逻辑删除')),
            ],
            options={
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
                'db_table': 'tb_article',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
                ('describe', models.CharField(max_length=100, verbose_name='描述')),
                ('category_image', models.ImageField(null=True, upload_to='', verbose_name='分类图片')),
            ],
            options={
                'verbose_name_plural': '分类',
                'verbose_name': '分类',
                'db_table': 'tb_category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50, verbose_name='评论内容')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article', verbose_name='文章')),
            ],
            options={
                'verbose_name_plural': '评论',
                'verbose_name': '评论',
                'db_table': 'tb_comment',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名称')),
            ],
            options={
                'verbose_name_plural': '标签',
                'verbose_name': '标签',
                'db_table': 'tb_tag',
            },
        ),
    ]