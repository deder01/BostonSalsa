# .. Imports

# Django apps
from django.contrib.auth import update_session_auth_hash

# Third party apps
from rest_framework import serializers

# Project apps
from account.models import Account

# .. End Imports


# Account Serlializer
class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('about_me', 'confirm_password', 'created_at', 'email', 'facebook', 'first_name', 'id', 'last_name', 'password', 'phone_number', 'twitter', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

        def create(self, validated_data):
            return Account.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.abc = validated_data.get('abc', instance.abc)
            instance.about_me = validated_data.get('about_me', instance.about_me)
            instance.facebook = validated_data.get('facebook', instance.facebook)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.phone_number = validated_data.get('phone_number', instance.phone_number)
            instance.twitter = validated_data.get('twitter', instance.twitter)

            instance.save()

            password = validated_data.get('password', None)
            confirm_password = validated_data.get('confirm_password', None)

            if password and confirm_password and password == confirm_password:
                instance.set_password(password)
                instance.save()
                update_session_auth_hash(self.context.get('request'), instance)

            return instance
