from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import JournalistModel, CategoryModel, ArticleModel

class JournalistSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=JournalistModel.objects.all(), message="This user already exists")
        ]
    )
    
    class Meta:
        model = JournalistModel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    image_select = serializers.SerializerMethodField()  # This will handle Cloudinary URL

    author_email = serializers.EmailField(write_only=True)
    author_email_display = serializers.EmailField(source='author.email', read_only=True)

    category_name = serializers.CharField(write_only=True)
    category_name_display = serializers.CharField(source='category.cat_name', read_only=True)

    class Meta:
        model = ArticleModel
        fields = [
            'id', 'title', 'description', 'location', 'published_on',
            'author_email',
            'image_select',
            'author_email_display',
            'category_name',
            'category_name_display',
        ]

    def get_image_select(self, obj):
        if obj.image_select:
            return obj.image_select.url
        return None

    def create(self, validated_data):
        author_email = validated_data.pop('author_email')
        category_name = validated_data.pop('category_name')

        try:
            author = JournalistModel.objects.get(email=author_email)
        except JournalistModel.DoesNotExist:
            raise serializers.ValidationError({"author_email": f"No journalist found with email '{author_email}'."})
        
        try:
            category = CategoryModel.objects.get(cat_name=category_name)
        except CategoryModel.DoesNotExist:
            raise serializers.ValidationError({"category_name": f"No category found with name '{category_name}'."})

        article = ArticleModel.objects.create(author=author, category_name=category, **validated_data)
        return article
