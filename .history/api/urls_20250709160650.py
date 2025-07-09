# api/urls.py

from django.urls import path
from .views import result_list_create, result_detail_update_delete

GAME_ORDER = [
    'game0', # 完整测试加载页
    'game1', # 日期游戏
    'game2', # 选词填空
    'game3', # 迷宫游戏
    'game4', # 舒尔特方格
    'game5', # 记忆棋盘
    'game6', # 分类游戏
    'game7', # 延迟回忆
    # ... 如果还有更多游戏，继续添加它们的URL名字
]

urlpatterns = [
    #  /api/results/ -> 用于获取列表和创建新条目
    path('results/', result_list_create, name='result-list-create'),
    
    #  /api/results/<id>/ -> 用于获取、更新、删除单个条目
    path('results/<uuid:id>/', result_detail_update_delete, name='result-detail-update-delete'),
]