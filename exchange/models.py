from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    contact = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    average_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    
    date_joined = models.DateTimeField(default=timezone.now)
    terms_agreed = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = UserManager()  # Ensure your UserManager is properly defined
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
    
    def get_short_name(self):
        return self.first_name or self.username

class PaymentMethod(models.Model):
    payment_method_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
    account_details = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.provider} - {self.user.email}"

class Item(models.Model):
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Like New', 'Like New'),
        ('Used', 'Used'),
        ('Refurbished', 'Refurbished'),
    ]

    LISTING_TYPE_CHOICES = [
        ('Sell', 'Sell'),
        ('Exchange', 'Exchange'),
    ]

    item_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)  # Add choices if needed
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPE_CHOICES)
    is_available = models.BooleanField(default=True)
    date_listed = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='item_pictures/', null=True, blank=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ItemTag(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.title} - {self.tag.name}"

class Proposal(models.Model):
    proposal_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_proposals')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_proposals')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Proposal from {self.sender.email} to {self.receiver.email}"

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    proposal = models.OneToOneField(Proposal, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_id}"

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_given')
    reviewee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_received')
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.review_id} by {self.reviewer.email}"

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.notification_id} for {self.user.email}"