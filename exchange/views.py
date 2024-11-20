from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from rest_framework import viewsets
from .models import (
    User, PaymentMethod, Item, Tag, ItemTag,
    Proposal, Transaction, Review, Notification
)
from .serializers import (
    UserSerializer, PaymentMethodSerializer, ItemSerializer, TagSerializer,
    ItemTagSerializer, ProposalSerializer, TransactionSerializer,
    ReviewSerializer, NotificationSerializer
)

def signup_step1(request):
    if request.method == 'POST':
        # Process form data and redirect to step 2
        return redirect('exchange:signup_step2')
    return render(request, 'exchange/signup_page1.html')  # Include 'exchange/' in the template path

def signup_step2(request):
    if request.method == 'POST':
        # Process form data and create the user
        return redirect('exchange:login')
    return render(request, 'exchange/signup_page2.html')  # Include 'exchange/' in the template path

def login_view(request):
    if request.method == 'POST':
        return redirect('exchange:homepage')
    return render(request, 'exchange/login.html')

def logout_view(request):
    logout(request)
    return redirect('exchange:login')

def home_view(request):
    return render(request, 'exchange/homepage.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class ItemTagViewSet(viewsets.ModelViewSet):
    queryset = ItemTag.objects.all()
    serializer_class = ItemTagSerializer

class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer