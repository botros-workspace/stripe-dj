from django.contrib import admin
from django.urls import path
from product.views import CreateCheckoutSessionView, ProductLandingPageView, PaymentCancelView, PaymentSuccessView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name ='create-checkout-session'),
    path('', ProductLandingPageView.as_view(), name = 'landing-page'),
    path('success/', PaymentSuccessView.as_view(), name = 'success'),
    path('cancel/', PaymentCancelView.as_view(), name = 'cancel'),
]
