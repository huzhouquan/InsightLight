# api/models.py

import uuid
from django.db import models

class AssessmentResult(models.Model):
    # 使用UUID作为主键，便于分享且更安全
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # 认知域得分
    visuospatial = models.FloatField(default=0, verbose_name="视空间")
    naming = models.FloatField(default=0, verbose_name="命名")
    memory = models.FloatField(default=0, verbose_name="记忆")
    attention = models.FloatField(default=0, verbose_name="注意")
    language = models.FloatField(default=0, verbose_name="语言")
    abstraction = models.FloatField(default=0, verbose_name="抽象")
    delayed_recall = models.FloatField(default=0, verbose_name="延迟回忆")
    orientation = models.FloatField(default=0, verbose_name="定向能力")

    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        # 在后台管理中显示一个可读的名称
        return f"评估结果 - {self.created_at.strftime('%Y-%m-%d %H:%M')}"