from rest_framework import serializers

from .models import Item, CategoryItem, ItemThroughIp, Comment, Favorite, MenuItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryItem
        fields = ('name',)


class CommentPostPostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'


class CommentGetPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('name', 'description', 'rating', 'image')


class MenuGetPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ('image', )

class ItemGetSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')
    city = serializers.CharField(source='city.name')
    category = serializers.CharField(source='category.name')
    views = serializers.IntegerField(source='total_views')

    class Meta:
        model = Item
        fields = '__all__'


class ItemPostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Item
        fields = '__all__'


class TopThreeItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    city = serializers.CharField(source='city.name')

    class Meta:
        model = Item
        fields = ('id', 'image', 'city', 'title', 'category', 'rating')


class SingleItemSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')
    city = serializers.CharField(source='city.name')
    category = serializers.CharField(source='category.name')
    views = serializers.IntegerField(source='total_views')
    comments = CommentGetPostSerializer(many=True)
    menu = MenuGetPostSerializer(many=True)

    class Meta:
        model = Item
        fields = '__all__'


class LastViewsItemSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='item.title')
    image = serializers.ImageField(source='item.image')
    rating = serializers.FloatField(source='item.rating')
    category = serializers.CharField(source='item.category.name')

    class Meta:
        model = ItemThroughIp
        fields = ('id', 'item', 'category', 'title', 'image', 'rating')


class FavoriteGETSerializer(serializers.ModelSerializer):
    item = ItemGetSerializer()
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoritePOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
