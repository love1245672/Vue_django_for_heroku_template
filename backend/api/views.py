from django.shortcuts import render
#from .models import Info,Customers,Application,Modules,Groups,Region,Products,Sn,Users,Edit
# Create your views here.
from django.http import HttpResponse

# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def show_all(request):#根據當前用戶所在群組權限將主畫面資料傳入
    return HttpResponse("OK")