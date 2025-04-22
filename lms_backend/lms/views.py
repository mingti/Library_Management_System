from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from lms.models import Book
from lms.serialzer import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
