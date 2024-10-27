from django.contrib import admin
from .models import User, PaymentMethod, Item, Tag, ItemTag, Proposal, Transaction, Review, Notification

admin.site.register(User)
admin.site.register(PaymentMethod)
admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(ItemTag)
admin.site.register(Proposal)
admin.site.register(Transaction)
admin.site.register(Review)
admin.site.register(Notification)