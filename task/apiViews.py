from rest_framework import generics
from .models import TaskModel
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class CreateTaskAPI(generics.CreateAPIView): #the create new task Class is created
    serializer_class = TaskSerializer #Json Objet is cteated
    queryset = TaskModel.objects.all() #DB is queried & task is created



class ListTasksAPI(generics.ListAPIView): #Task L
    serializer_class = TaskSerializer #JSON OBJ is created
    queryset = TaskModel.objects.all() #DB is queried



class UpdateTaskAPI(APIView):
    def put(self, request, id, *arg, **kwargs): #this is the where the update function is created
        task = TaskModel.objects.get(id=id) # the task model is queried using the particular task id
        if not task: # her the Db is checked it that particular task doesnt exist
            return Response({'msg': 'data doesnt exists'},status=status.HTTP_400_BAD_REQUEST, ) # if the task isn't found an err msg is retured  
        data = { # here the data to be upodated is created
            'task': request.data.get('name'), # here the the name field is gotten from the request  
            #'completed': request.data.get('completed')  # here the the completed field is gotten from the request
        }
        serializer = TaskSerializer(instance = task, data=data, partial = True) # a JSON object is created for the data to be updated
        if serializer.is_valid(): # the JSON object is checked if valid
            serializer.save() # the JSON object saved
            return Response(serializer.data, status=status.HTTP_200_OK) # a success response is returned to the user
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # an error response is returned if the operation wasnt successful
    

class GetTaskByIdAPI(APIView):
    def get(self, request, id=None): # the function for getting a particular task is created
        queryset = TaskModel.objects.get(id=id) # the DB is queried using the task id
        serializer = TaskSerializer(queryset) # a JSON object is created for the data to be updated
        res = { # response obj is created
            'msg': 'task fetched successful', #  
            'status': status.HTTP_200_OK ,
            'data': serializer.data
        }
        return Response(res) #response is outputted
'''
class UpdateTaskAPI(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()

'''


class DeleteTaskAPI(APIView):
    def delete(self, request, id=None): # delete function is created
        tasks = get_object_or_404(TaskModel, id=id) #DB is query using the ID
        tasks.delete() # the task is deleted
        serializer = TaskSerializer(tasks) #JSON obj is created
        res = { #res obj is created
             'msg': 'deleted successful',
            'status': status.HTTP_200_OK ,
              
        }   
        return Response(res) # res is returned
    



class TaskAPIView(APIView):
    def get_object(self, id):
        try:
            return TaskModel.objects.get(id=id)
        except TaskModel.DoesNotExist:
            return None
        
    def get(self, request, id, *arg, **kwargs):
        task = TaskModel.objects.get(id=id)
        serializer = TaskSerializer(task)
        res = {
             'msg': 'deleted successful',
            'status': status.HTTP_200_OK ,
              'data': serializer.data
        }   
        return Response(res)
    
    def put(self, request, id, *arg, **kwargs):
        task = TaskModel.objects.get(id=id)
        if not task:
            return Response({'msg': 'data doesnt exists'},status=status.HTTP_400_BAD_REQUEST, ) 
        data = {
            'task': request.data.get('name'), 
        }
        serializer = TaskSerializer(instance = task, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        task = self.get_object(id)
        if not task:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        task.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )