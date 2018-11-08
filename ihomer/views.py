from django.shortcuts import render
from ihomer.models import NodePost


# Create your views here.
def node_index(request):
    node_list = NodePost.objects.all()  # 获取所有数据
    return render(request, 'index.html', {'node_list': node_list})   # 返回index.html页面


def about_us(request):
    return render(request, 'about.html')


#def connect_us(request):
#    return render(request, 'connet.html')


# Create your views here.
