from rest_framework import serializers
from .models import Product, Category, Colors, Gender, CustomUser, SubCategory
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ProductSerializer(
    serializers.ModelSerializer):  # Вывод товара конкретной категории /api/products/?category=сategory_name
    color = serializers.StringRelatedField(many=True)
    gender = serializers.StringRelatedField(many=True)
    size = serializers.StringRelatedField(many=True)
    manufacturer = serializers.StringRelatedField(many=False)
    category = serializers.StringRelatedField(many=False)
    sub_category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = (
            'manufacturer', 'category', 'sub_category', 'name', 'size', 'color', 'price', 'description', 'gender',
            'quantity',
            'image',
            'seen',
            'date_published', 'counter', 'unique_id', 'popularity_counter')


#     def to_representation(self, instance):
#         rep = super(ProductsSerializer, self).to_representation(instance)
#         rep['category'] = instance.category.name
#         rep['gender'] = instance.gender.gender
#         return rep


class CategoriesSerializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ('name', 'content')


class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('sub_name',)


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ('color',)


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ('gender',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
