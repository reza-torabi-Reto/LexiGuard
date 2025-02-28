from django.urls import path
from .views import *

urlpatterns = [
    path('words/', WordsView.as_view(), name='words-dictionary'),
    path('words-of-user/<int:user_id>', WordsView.as_view(), name='words-dictionary'),
    path('create/', WordsView.as_view(), name='create-dictionary'),
    path('update/<int:id>', WordsView.as_view(), name='create-dictionary'),
    path('delete/<int:id>', WordsView.as_view(), name='create-dictionary'),
]
