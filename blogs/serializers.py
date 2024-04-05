from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'