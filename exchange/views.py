from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignUpStep1Form, SignUpStep2Form, ProfileSettingsForm, ItemForm
from rest_framework import viewsets
from django.contrib import messages
from django.urls import reverse
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
        form = SignUpStep1Form(request.POST)
        if form.is_valid():
            # Store step 1 data in session
            request.session['signup_email'] = form.cleaned_data['email']
            request.session['signup_username'] = form.cleaned_data['username']
            request.session['signup_password'] = form.cleaned_data['password']
            return redirect('exchange:signup_step2')
    else:
        form = SignUpStep1Form()
    return render(request, 'exchange/signup_page1.html', {'form': form})

def signup_step2(request):
    if request.method == 'POST':
        form = SignUpStep2Form(request.POST)
        if form.is_valid():
            # Retrieve step 1 data from session
            email = request.session.get('signup_email')
            username = request.session.get('signup_username')
            password = request.session.get('signup_password')

            if not all([email, username, password]):
                # Redirect back to step 1 if data is missing (user might have skipped it)
                return redirect('exchange:signup_step1')

            # Create user object
            try:
                user = User.objects.create_user(
                    email=email,
                    username=username,
                    password=password,
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    city=form.cleaned_data['city'],
                    state=form.cleaned_data['state'],
                    country=form.cleaned_data['country'],
                    zip_code=form.cleaned_data['zip_code'],
                    terms_agreed=form.cleaned_data['terms_agreed'],
                )
                # Clear the session data after successful signup
                del request.session['signup_email']
                del request.session['signup_username']
                del request.session['signup_password']
                # Log the user in and redirect to login
                return redirect('exchange:login')
            except Exception as e:
                # Handle errors (e.g., database error, duplicate email)
                form.add_error(None, f"Error creating user: {e}")
                return render(request, 'exchange/signup_page2.html', {'form': form})

    else:
        form = SignUpStep2Form()

    return render(request, 'exchange/signup_page2.html', {'form': form})

def login_view(request):
    invalid_fields = []  # Track which fields are invalid
    show_login = False   # Flag to indicate if the login form should be visible

    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)

        if form.is_valid():
            if form.login():  # Perform the login
                return redirect('exchange:homepage')  # Redirect on successful login
        else:
            show_login = True  # Show the login form on failed login
            # Add invalid fields to the list
            if form.errors.get('username'):
                invalid_fields.append('username')
            if form.errors.get('password'):
                invalid_fields.append('password')
    else:
        form = LoginForm()

    # Pass the form, invalid fields, and show_login flag to the template
    context = {
        'form': form,
        'invalid_fields': invalid_fields,
        'signup_url': reverse('exchange:signup_step1'),
        'show_login': show_login  # Ensure the login form stays visible
    }
    return render(request, 'exchange/login.html', context)

def landing(request):
    return render(request, 'exchange/landing.html')

def logout_view(request):
    logout(request)
    return redirect('exchange:login')

@login_required
def home_view(request):
    items = Item.objects.filter(is_available=True).select_related('user')
    context = {
        'items': items
    }
    return render(request, 'exchange/homepage.html', context)

@login_required
def user_profile(request, username):
    user = request.user
    items = Item.objects.filter(user=user, is_available=True).order_by('-date_listed')
    
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = user
            new_item.save()
            return redirect('exchange:user_profile', username=user.username)
    else:
        form = ItemForm()
    
    context = {
        'user': user,
        'items': items,
        'form': form,
    }
    return render(request, 'exchange/user_profile.html', context)

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('exchange:user_profile', username=request.user.username)
    else:
        form = ItemForm()
    
    return render(request, 'exchange/add_item.html', {'form': form})

@login_required
def user_profile_settings(request):
    user = request.user  # Get the logged-in user

    if request.method == 'POST':
        form = ProfileSettingsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('exchange:user_profile_settings')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileSettingsForm(instance=user)

    return render(request, 'exchange/user_profile_settings.html', {'form': form, 'user': user})

@login_required
def upload_avatar(request):
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')

        if avatar:
            user = request.user
            user.profile_picture = avatar
            user.save()
            messages.success(request, 'Your profile picture has been updated.')
        else:
            messages.error(request, 'Please select an image to upload.')
        
        return redirect('exchange:user_profile_settings')

    return redirect('exchange:user_profile_settings')

# Rest of your ViewSets remain the same...
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