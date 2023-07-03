from rest_framework import serializers
from .models import Article, New, NewCategorie, Historie

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title','description', 'key', 'image')
    
class NewCategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCategorie
        fields = ('id', 'name')

class NewSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset = New.objects)
    class Meta:
        model = New
        fields = ('id', 'name', 'description', 'image','pub_date', 'category')

class HistorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historie
        fields = ('id', 'title', 'description', 'street', 'image', 'history_title', 'history_description', 'history_image')