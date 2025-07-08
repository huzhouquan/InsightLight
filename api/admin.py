# api/admin.py

from django.contrib import admin
from .models import AssessmentResult

# 创建一个自定义的管理类来改善显示效果
@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    # 在列表页显示的字段
    list_display = (
        'id', 'created_at', 'visuospatial', 'naming', 'memory', 
        'attention', 'language', 'abstraction', 'delayed_recall', 'orientation'
    )
    # 设置只读字段，因为通常这些数据不应该在后台手动修改
    readonly_fields = ('id', 'created_at')
    # 按创建时间排序
    ordering = ('-created_at',)