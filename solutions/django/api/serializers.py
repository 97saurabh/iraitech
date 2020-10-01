from rest_framework import serializers

class Serializer(serializers.Serializer):
    x = serializers.IntegerField()
    a = serializers.IntegerField()
    
    def validate(self, data):
        if data['x'] == 0:
            raise serializers.ValidationError({'Eror': "x can not be zero"})
        return data