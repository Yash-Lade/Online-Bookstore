from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import Cart
from books.models import Book


class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):

        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found"}, status=400)

        if not cart.items.exists():
            return Response({"error": "Cart is empty"}, status=400)

        total_price = 0
        order = Order.objects.create(user=request.user, total_price=0)

        for item in cart.items.all():

            book = item.book

            if book.stock < item.quantity:
                return Response(
                    {"error": f"Not enough stock for {book.title}"},
                    status=400
                )

            # Decrease stock
            book.stock -= item.quantity
            book.save()

            # Calculate total
            item_total = book.price * item.quantity
            total_price += item_total

            # Create order item
            OrderItem.objects.create(
                order=order,
                book=book,
                quantity=item.quantity,
                price=book.price
            )

        order.total_price = total_price
        order.save()

        # Clear cart
        cart.items.all().delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=201)

# View Odrer History
class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
