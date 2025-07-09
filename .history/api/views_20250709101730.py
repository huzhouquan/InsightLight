# api/views.py

import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt # 用于允许外部POST请求
from .models import AssessmentResult
from django.shortcuts import render,redirect


def index_view(request):
    """
    This view serves the main index.html file.
    """
    return render(request, 'index.html')
def frontendchoose_view(request):

    return render(request, 'frontendchoose.html')

def game0_view(request):
    # 1. 创建一个新的评估结果对象
    new_result = AssessmentResult.objects.create()
    
    # 2. 将新对象的ID（转换为字符串）存入当前用户的session中
    #    request.session 就像一个字典，你可以自由存取
    request.session['result_id'] = str(new_result.id)
    
    # --- 渲染模板 ---
    context = {
        'game_name': '完整测试',
        'game_id': 0,
        'result_id': new_result.id # 将ID也传递给当前模板
    }
    return render(request, 'game0.html',context)
def game1_view(request):
    result_id = request.session.get('result_id')
    context = {
        'game_id': 1,
        'result_id': result_id # 将我们从session中取出的ID传递给模板
    }
    return render(request, 'game1.html',context)
def game2_view(request):
    result_id = request.session.get('result_id')
    context = {
        'game_id': 2,
        'result_id': result_id # 将我们从session中取出的ID传递给模板
    }
    return render(request, 'game2.html',context)
def game3_view(request):
    result_id = request.session.get('result_id')
    context = {
        'game_id': 3,
        'result_id': result_id # 将我们从session中取出的ID传递给模板
    }
    return render(request, 'game3.html')
def game4_view(request):
    result_id = request.session.get('result_id')
    context = {
        'game_id': 4,
        'result_id': result_id # 将我们从session中取出的ID传递给模板
    }
    return render(request, 'game4.html')
def game5_view(request):
    result_id = request.session.get('result_id')
    context = {
        'game_id': 5,
        'result_id': result_id # 将我们从session中取出的ID传递给模板
    }
    return render(request, 'game5.html')
def game6_view(request):
    result_id = request.session.get('result_id')
    context = {
        'game_id': 6,
        'result_id': result_id # 将我们从session中取出的ID传递给模板
    }
    return render(request, 'game6.html')
def game7_view(request):
    result_id = request.session.get('result_id')
    context = {
        'game_id': 7,
        'result_id': result_id # 将我们从session中取出的ID传递给模板
    }
    return render(request, 'game7.html')
@csrf_exempt # 注意：这在开发中很方便，但在生产环境中需要更安全的认证方式
def result_list_create(request):
    """
    处理“获取所有结果列表”和“创建一个新结果”的逻辑。
    - GET: 返回所有结果的列表。
    - POST: 创建一个新的结果。
    """
    if request.method == 'GET':
        results = AssessmentResult.objects.all().order_by('-created_at')
        # 将查询集（QuerySet）转换成一个字典列表
        data = list(results.values(
            'id', 'visuospatial', 'naming', 'memory', 'attention', 'language',
            'abstraction', 'delayed_recall', 'orientation', 'created_at'
        ))
        return JsonResponse(data, safe=False) # safe=False 允许返回列表

    elif request.method == 'POST':
        try:
            # 从请求体中加载JSON数据
            data = json.loads(request.body)
            
            # 创建新的 AssessmentResult 对象
            new_result = AssessmentResult.objects.create(
                visuospatial=data.get('visuospatial', 0),
                naming=data.get('naming', 0),
                memory=data.get('memory', 0),
                attention=data.get('attention', 0),
                language=data.get('language', 0),
                abstraction=data.get('abstraction', 0),
                delayed_recall=data.get('delayed_recall', 0),
                orientation=data.get('orientation', 0)
            )
            # 返回新创建的对象信息，包括它的ID
            return JsonResponse({
                'id': new_result.id,
                'message': 'Result created successfully'
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def result_detail_update_delete(request, id):
    """
    处理针对“单个”结果的“获取(GET)、更新(PATCH)、删除(DELETE)”逻辑。
    """
    try:
        # 先根据ID从数据库找到要操作的对象
        result = AssessmentResult.objects.get(id=id)
    except AssessmentResult.DoesNotExist:
        # 如果找不到，返回404错误
        return JsonResponse({'error': 'Result not found'}, status=404)

    # --- 处理 GET 请求 (获取单个结果) ---
    if request.method == 'GET':
        response_data = {
            'id': result.id,
            'visuospatial': result.visuospatial,
            'naming': result.naming,
            'memory': result.memory,
            'attention': result.attention,
            'language': result.language,
            'abstraction': result.abstraction,
            'delayed_recall': result.delayed_recall,
            'orientation': result.orientation,
            'created_at': result.created_at
        }
        return JsonResponse(response_data)
        
    # --- 处理 PATCH 请求 (更新单个结果) ---
    elif request.method == 'PATCH':
        try:
            # 从请求体中加载JSON数据
            data = json.loads(request.body)
            
            # 遍历传入的数据字典 (如 {'memory': 95, 'naming': 90})
            for key, value in data.items():
                # 安全地检查对象是否真的有这个属性，然后更新它
                if hasattr(result, key):
                    setattr(result, key, value)
            
            result.save() # 保存所有更改到数据库
            
            # 返回一个成功的消息
            return JsonResponse({'message': 'Result updated successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=400)

    # --- 处理 DELETE 请求 (删除单个结果) ---
    elif request.method == 'DELETE':
        result.delete()
        return HttpResponse(status=204) # 204 No Content 是删除成功的标准响应

    # --- 如果是其他方法 (如 POST, PUT)，则返回不允许 ---
    else:
        return JsonResponse({'error': f'Method {request.method} not allowed'}, status=405)