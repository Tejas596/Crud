from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birthdate']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested serializer for Author

    class Meta:
        model = Book
        fields = ['id', 'title', 'published_date', 'author']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        instance.title = validated_data.get('title', instance.title)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        author, created = Author.objects.get_or_create(**author_data)
        instance.author = author
        instance.save()
        return instance
