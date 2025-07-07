from rest_framework import serializers
from .models import AssessmentResult

class AssessmentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentResult
        # 定义需要包含在API中的所有字段
        fields = [
            'id', 'visuospatial', 'naming', 'memory', 'attention', 
            'language', 'abstraction', 'delayed_recall', 'orientation', 
            'created_at'
        ]