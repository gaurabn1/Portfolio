from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<slug:slug>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
]