from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world ! ")


def dabing(request):
    context = {}
    context['hello'] = "my cat is '大饼', a cute cat"
    return render(request, 'dabing.html', context)

def cat(request):
    time_now = datetime.datetime.now()
    cat_list = [{"name": "小黑", "color": "黑色", "character": "活泼"},{"name": "佩奇", "color": "粉色", "character": "可爱"}, {"name": "猪猪", "color": "白色", "character": "文静"}]
    info = "我的大饼"
    my_cat_info = {"name": "大饼", "color": "灰白色", "meowing": "嗷呜～", "character": "超可爱"}
    return render(request, 'dabing.html', {'my_cat': my_cat_info, "time_now": time_now, "cat_list": cat_list})
