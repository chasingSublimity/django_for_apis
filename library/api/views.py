from rest_framework import generics

from books.models import Book
from .serializers import BookSerializer

# read only endpoint for all books
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer