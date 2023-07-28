from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# def hello_world(request):
#     return HttpResponse("Hello, world!")

# def display_even_nums(request):
#     response = ""
#     nums = [1,2,3,4,5,6,7,8,9]
#     for i in nums:
#         remainder = i % 2
#         if remainder == 0:
#             response += str(i) + "<br/>"
            
#     return HttpResponse(response)

@api_view(['GET','POST'])
def books(request):
    return Response('list of the books', status=status.HTTP_200_OK)


class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message":"list of the books by " + author}, status.HTTP_200_OK)
        return Response({"message":"list of the books"}, status.HTTP_200_OK)
    
    def post(self, request):
        return Response({"title":request.data.get('title')}, status.HTTP_201_CREATED)
    
    
class Book(APIView):
    def get(self,request, pk):
        return Response({"message":"single book with id " + str(pk)}, status.HTTP_200_OK)
    
    def put(self, request, pk):
        return Response({"title":request.data.get('title')}, status.HTTP_200_OK)