from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from .models import Rating
from django.conf import settings

User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=Rating)
def update_average_rating_on_save(sender, instance, **kwargs):
    ratee = instance.ratee
    average = Rating.objects.filter(ratee=ratee).aggregate(Avg('rating'))['rating__avg'] or 0.0
    ratee.average_rating = round(average, 2)
    ratee.save(update_fields=['average_rating'])

@receiver(post_delete, sender=Rating)
def update_average_rating_on_delete(sender, instance, **kwargs):
    ratee = instance.ratee
    average = Rating.objects.filter(ratee=ratee).aggregate(Avg('rating'))['rating__avg'] or 0.0
    ratee.average_rating = round(average, 2)
    ratee.save(update_fields=['average_rating'])