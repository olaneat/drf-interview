from rest_framework import generics
from .models import TaskModel
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView


class CreateTaskAPI(generics.CreateAPIView):
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()



class ListTasksAPI(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()



class UpdateTaskAPI(APIView):
    def put(self, request, id=None):
        update_task = TaskModel.objects.filter(id=id)
        update_task.update()
        res = {
             'msg': 'task updated successful',
             'status': status.HTTP_200_OK 
        }
        return Response(res)
'''
class UpdateTaskAPI(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()

'''


class DeleteTaskAPI(APIView):
    def delete(self, request, id=None):
        tasks = TaskModel.objects.filter(id=id)
        tasks.delete()
        res = {
             'msg': 'deleted successful',
            'status': status.HTTP_200_OK             
        }   
        return Response(res)