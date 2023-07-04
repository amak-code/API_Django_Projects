from django.urls import path
from . import views

# urlpatterns = [path('hello/', views.hello_world, name='hello_world'),
# ]

urlpatterns = [path('numbers/', views.display_even_nums),
]
