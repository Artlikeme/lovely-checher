from rest_framework import serializers


class ModerationCitySerializer(serializers.Serializer):
    to_active = serializers.BooleanField()
    to_deactive = serializers.BooleanField()
    code = serializers.IntegerField()

    def save(self):
        to_active = self.validated_data['to_active']
        to_deactive = self.validated_data['to_deactive']
        code = self.validated_data['code']


class ModerationItemSerializer(serializers.Serializer):
    to_active = serializers.BooleanField()
    to_deactive = serializers.BooleanField()
    description = serializers.CharField(default='Some desc')

    def save(self):
        to_active = self.validated_data['to_active']
        to_deactive = self.validated_data['to_deactive']
        description = self.validated_data['description']
