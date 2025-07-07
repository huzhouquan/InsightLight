from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import AssessmentResult
from .serializers import AssessmentResultSerializer

# 用于创建新结果 (处理POST请求)
class ResultCreateView(generics.ListCreateAPIView): 
    queryset = AssessmentResult.objects.all()
    serializer_class = AssessmentResultSerializer

# 用于根据ID获取单个结果 (处理GET请求)
class ResultRetrieveView(generics.RetrieveAPIView):
    queryset = AssessmentResult.objects.all()
    serializer_class = AssessmentResultSerializer
    lookup_field = 'id' # 告诉DRF使用我们定义的UUID 'id' 来查找