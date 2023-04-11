from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView

from django.core.cache import cache

class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        cache_key = 'products'
        result = cache.get(cache_key, None)
        if not result:
            result = Product.objects.all()
            cache.set(cache_key, result)
        gender = self.request.query_params.get('gender', None)
        manufacturer = self.request.query_params.get('manufacturer', None)
        color = self.request.query_params.get('color', None)
        size = self.request.query_params.get('size', None)
        category = self.request.query_params.get('category', None)
        subcaterogy = self.request.query_params.get('sub_category', None)
        unique_id = self.request.query_params.get('unique_id', None)

        if unique_id is not None:
            result = result.filter(unique_id=unique_id)
        if gender is not None:
            result = result.filter(gender__gender=gender)
        if category is not None:
            result = result.filter(category__name=category)
        if subcaterogy is not None:
            result = result.filter(sub_category__sub_name=subcaterogy)
        if manufacturer is not None:
            result = result.filter(manufacturer__manufacturer=manufacturer)
        if color is not None:
            result = result.filter(color__color=color)
        if size is not None:
            result = result.filter(size__size=size)
        return result


class UserRegistration(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(['GET'])
def category_list_Api(request):
    if request.method == 'GET':
        data = Category.objects.all()
        serializer = CategoriesSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def subcategory_list_Api(request):
    if request.method == 'GET':
        data = SubCategory.objects.all()
        serializer = SubCategoriesSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def color_list_Api(request):
    if request.method == 'GET':
        data = Colors.objects.all()
        serializer = ColorsSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def gender_list_Api(request):
    if request.method == 'GET':
        data = Gender.objects.all()
        serializer = GenderSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
