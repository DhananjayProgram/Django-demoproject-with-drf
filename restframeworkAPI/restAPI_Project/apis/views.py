from django.shortcuts import render ,HttpResponse 
from django.http import  JsonResponse , Http404
from .models  import WatchList ,StreamPlatform
from .serializers import WatchListSerializer,StreamPlatformSerializer
from rest_framework import status , generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Generic and mixin 
class streamPlatformList(generics.ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

class streamPlatformDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
class movieList(generics.ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

class movieDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

# class based
# class streamPlatformList(APIView):
#     def get(self,request,format = None):
#         stream_all = StreamPlatform.objects.all()
#         stream_serialized = StreamPlatformSerializer(stream_all,many = True)
#         return Response(stream_serialized.data)
    
#     def post(self,request,format = None):
#         _data =request.data
#         serialized = StreamPlatformSerializer(data= _data)        
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data,status = status.HTTP_201_CREATED)
#         return Response(serialized.errors , status = status.HTTP_400_BAD_REQUEST)

# class streamPlatformDetail(APIView):
    
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return StreamPlatform.objects.get(pk=pk)
#         except StreamPlatform.DoesNotExist:
#             raise Http404

#     def get(self , request,pk, format = None):
#         stream_platform = self.get_object(pk)
#         serializer = StreamPlatformSerializer(stream_platform)
#         return Response(serializer.data)
    
#     def put(self , request,pk,format = None):
#         stream_platform = self.get_object(pk)
#         _data = request.data
#         serializer = StreamPlatformSerializer(stream_platform , data = _data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
#     def delete(self , request,pk,format = None):
#         stream_platform = self.get_object(pk)
#         stream_platform.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)



# function Based


# @api_view(["GET","POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movie_all = WatchList.objects.all()
#         movie = WatchListSerializer(movie_all,many = True)
#         return Response(movie.data)
    
#     if request.method == "POST":
#         _data = request.data
#         serializer = WatchListSerializer(_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status = status.HTTP_201_CREATED)
    
#     # return HttpResponse("Testing List View")

# def movie_detail(request,pk):
#     movie_list = WatchList.objects.get(id=pk)
#     serialized = WatchListSerializer(movie_list)
    
#     return JsonResponse(serialized.data)

# @api_view(["GET","POST"])
# def stream_list(request, format = None):
#     if request.method == "GET":
#         stream_all = StreamPlatform.objects.all()
#         stream_serialized = StreamPlatformSerializer(stream_all,many = True)
#         return Response(stream_serialized.data)
    
#     elif request.method == "POST":
#         _data =request.data
#         serialized = StreamPlatformSerializer(data= _data)        
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data,status = status.HTTP_201_CREATED)
#         return Response(serialized.errors , status = status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def stream_detail(request,pk , format =None):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try :
#         stream_platform = StreamPlatform.objects.get(id=pk)
#     except  StreamPlatform.DoesNotExist :
#         return Response(status = status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         serializer = StreamPlatformSerializer(stream_platform)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         _data = request.data
#         serializer = StreamPlatformSerializer(stream_platform , data = _data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         stream_platform.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
    