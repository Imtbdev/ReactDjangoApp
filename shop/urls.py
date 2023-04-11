from fullstackApp import settings
from .views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('api/products/', ProductList.as_view()),
    path('api/categories/', category_list_Api),
    path('api/subcategories/', subcategory_list_Api),
    path('api/colors/', color_list_Api),
    path('api/gender/', gender_list_Api),
    path('api/register/', UserRegistration.as_view()),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
