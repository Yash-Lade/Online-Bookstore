# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Avg

from .models import Review
from .serializers import ReviewSerializer
from books.models import Book


class CreateReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        book_id = request.data.get('book')

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)

        if Review.objects.filter(user=request.user, book=book).exists():
            return Response(
                {"error": "You have already reviewed this book."},
                status=400
            )

        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class BookReviewsView(APIView):

    def get(self, request, book_id):
        reviews = Review.objects.filter(book_id=book_id)
        serializer = ReviewSerializer(reviews, many=True)

        average = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']

        return Response({
            "average_rating": average,
            "reviews": serializer.data
        })
