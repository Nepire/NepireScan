from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
import socket
ip = []
domain1 = ['soft.acg.tv', 'i4.acg.tv', 'i2.acg.tv', 'img.acg.tv', 'send.acg.tv', 'stat.acg.tv', 'info.acg.tv', 'share.acg.tv', 'ad.acg.tv', 'h.acg.tv', 'i3.acg.tv', 'live.acg.tv', 's.acg.tv', 'events.acg.tv', 'i1.acg.tv', 'link.acg.tv', 'm.acg.tv', 'moe.acg.tv', 'pl.acg.tv',"static.acg.tv"]
domain = ['bw.bilibili.com', 'cm.bilibili.com', 'comic.bilibili.com', 'h.bilibili.com', 'game.bilibili.com', 'interface.bilibili.com', 'live.bilibili.com', 'api.live.bilibili.com', 'offline.bilibili.com', 'sitemap.bilibili.com', 'space.bilibili.com', 't.bilibili.com', 'test.live.bilibili.com', 'zb.bilibili.com', 'activity.bilibili.com', 'app.bilibili.com', 'baidu.bilibili.com', 'docs.bilibili.com', 'lvyou.bilibili.com', 'pay.bilibili.com']
def home(request):
    return render(request,'dashboard.html')

def icons(request):
    return render(request,'icons.html',{'domain':domain,'domain1':domain1})

def tables(request):
    return render(request,'tables.html')

def typography(request):
    return render(request,'typography.html')

# def domain_scan(request):
#     f = open('../data/bilibili/hdslb.net.txt')
#     domain=[]
#     for i in range(7):
#         tmp = f.readline()[:-1].replace(' ','')
#         domain.append(tmp.replace('\t',' '))
#     return domain


def port_scan(ip,port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(2)
    try:
        sk.connect((ip,port))
        return 200
    except Exception:
        return 404
    sk.close()
