# api/urls.py

from django.urls import path
from .views import result_list_create, result_detail_update_delete


urlpatterns = [
    #  /api/results/ -> 用于获取列表和创建新条目
    path('results/', result_list_create, name='result-list-create'),
    
    #  /api/results/<id>/ -> 用于获取、更新、删除单个条目
    path('results/<uuid:id>/', result_detail_update_delete, name='result-detail-update-delete'),
]