from django.db import models

class Book(models.Model):

    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('sci-fi', 'Sci-Fi'),
        ('biography', 'Biography'),
        ('fantasy', 'Fantasy'),
        ('romance','Romance'),
    ]

    title = models.CharField(max_length=255, db_index=True)
    author = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
