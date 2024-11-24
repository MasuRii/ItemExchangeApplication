from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'exchange'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'payment-methods', views.PaymentMethodViewSet, basename='paymentmethod')
router.register(r'items', views.ItemViewSet, basename='item')
router.register(r'tags', views.TagViewSet, basename='tag')
router.register(r'item-tags', views.ItemTagViewSet, basename='itemtag')
router.register(r'proposals', views.ProposalViewSet, basename='proposal')
router.register(r'transactions', views.TransactionViewSet, basename='transaction')
router.register(r'reviews', views.ReviewViewSet, basename='review')
router.register(r'notifications', views.NotificationViewSet, basename='notification')

urlpatterns = [
    path('signup/step1/', views.signup_step1, name='signup_step1'),
    path('signup/step2/', views.signup_step2, name='signup_step2'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('homepage/', views.home_view, name='homepage'),
    path('', views.landing, name='landing'),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]