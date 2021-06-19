from rest_framework import fields, serializers

from. models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('name', 'price', 'description', 'created_at', 'updated_at')