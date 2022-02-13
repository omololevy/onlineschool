from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['phone'] = user.phone
        return token


class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(
        required=True)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'phone','password', 'password2', 'email', 'name', 'lastname', 'gender', 'sinf')
        extra_kwargs = {
            'name': {'required': True},
            'lastname': {'required': True},
            'sinf': {'required': True},
            'gender': {'required': True},
        }


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            phone=validated_data['phone'],
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            gender=validated_data['gender'],
            sinf=validated_data['sinf']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user