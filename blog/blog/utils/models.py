# -*- coding:utf8 -*-
from django.db import models
import django.utils.timezone as timezone


class BaseModel(models.Model):
    """为模型类补充字段"""
    create_time = models.DateTimeField(default = timezone.now, editable=True, verbose_name="创建时间")
    update_time = models.DateTimeField(default = timezone.now, editable=True, verbose_name="更新时间")

    class Meta:
        # 说明是抽象模型类, 用于继承使用，数据库迁移时不会创建BaseModel的表
        abstract = True
