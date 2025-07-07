from django.db import models

# Create your models here.
# api/models.py
import uuid
from django.db import models

class AssessmentResult(models.Model):
    # 使用UUID作为分享链接的ID，更安全且不会暴露数据顺序
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # 认知域得分
    visuospatial = models.FloatField(default=0) # 视空间
    naming = models.FloatField(default=0) # 命名
    memory = models.FloatField(default=0) # 记忆
    attention = models.FloatField(default=0) # 注意
    language = models.FloatField(default=0) # 语言
    abstraction = models.FloatField(default=0) # 抽象
    delayed_recall = models.FloatField(default=0) # 延迟回忆
    orientation = models.FloatField(default=0) # 定向能力

    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result {self.id}"