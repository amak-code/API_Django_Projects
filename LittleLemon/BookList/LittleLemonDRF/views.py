from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import Response

# def hello_world(request):
#     return HttpResponse("Hello, world!")

def display_even_nums(request):
    response = ""
    nums = [1,2,3,4,5,6,7,8,9]
    for i in nums:
        remainder = i % 2
        if remainder == 0:
            response += str(i) + "<br/>"
            
    return HttpResponse(response)