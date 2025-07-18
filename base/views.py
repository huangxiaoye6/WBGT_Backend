import os

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from WBGT_backend import settings
from base.models import User, Content
from base.serializers import ContentSerializer
from utils.auth import create_token
from utils.content import login, get_data, device_status, weather


# Create your views here.

class LoginView(APIView):
    authentication_classes = []
    def post(self, request):
        username = request.data.get('username')
        pwd=request.data.get('password')
        user=User.objects.filter(username=username).first()
        if user:
            user_check=User.objects.filter(username=username,password=pwd).first()
            if user_check:
                payload = {
                    'username': user_check.username,
                    'uid': user_check.uid,
                }
                token = create_token(payload)
                return Response(data={'msg':'登录成功',"token":token,'code':1000})
            else:
                return Response(data={'msg': '登录失败', 'error': '密码错误', 'code': 1002})
        else:
            return Response(data={'msg':'登录失败','error':'用户不存在','code':1001})

class DataView(APIView):
    def get(self,request):
        content=Content.objects.first()
        serializer = ContentSerializer(content)
        data = serializer.data
        data['imgURL'] = 'https://api.023runclub.com{0}'.format(data['imgURL'])
        return Response(data={'msg':'查询成功','data':data})
    def post(self,request):
        content=Content.objects.first()
        serializer = ContentSerializer(instance=content,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'msg':'修改成功','data':serializer.data})
        else:
            return Response(data={'msg':'修改失败','error':serializer.errors,'code':1005})

class DataInfoView(APIView):
    authentication_classes = []
    def get(self,request):
        try:
            token = login()
            temperature_info=get_data(token)
            status=device_status(token)
            data={
                'status': status,
                'temperatureInfo':temperature_info,
            }
            return Response(data={'msg': '查询成功', 'data': data})
        except Exception as e:
            return Response(data={'msg': '查询失败', 'error': e,'code': 1005})

class ImgView(APIView):
    """
    post:图片上传
    """
    authentication_classes = []
    def post(self, request):
        content = Content.objects.first()
        serializer = ContentSerializer(instance=content, data=request.data, partial=True)
        if serializer.is_valid():
            path = os.path.join(settings.MEDIA_ROOT, str(content.imgURL))
            if os.path.exists(path) and content.imgURL:
                os.remove(path)
            serializer.save()
            data=serializer.data
            data['imgURL'] = 'https://api.023runclub.com{0}'.format(data['imgURL'])
            return Response(data={'msg': '上传成功', 'data': data, 'code': 200, })
        else:
            return Response(data={'msg': '上传失败', 'error': serializer.errors, 'code': 401})
class ImgShowView(APIView):
    """
    get:图片查询
    """
    authentication_classes = []

    def get(self, request, img_path):
        path = os.path.join(settings.MEDIA_ROOT, 'img', img_path)
        if os.path.exists(path):
            with open(path, 'rb') as f:
                data = f.read()
                return HttpResponse(content=data, content_type='image/jpeg')
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



