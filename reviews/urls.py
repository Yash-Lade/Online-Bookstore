from django.urls import path
from .views import CreateReviewView, BookReviewsView

urlpatterns = [
    path('create/', CreateReviewView.as_view()),
    path('<int:book_id>/', BookReviewsView.as_view()),
]
