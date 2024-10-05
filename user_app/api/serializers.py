from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input-type": "password"}, write_only=True)    
    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password": { "write_only": True }
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError("Password and Password2 should be the same.")

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({"error": "Email already exists."})
        
        newUserInfo = {
            "username": self.validated_data["username"],
            "email": self.validated_data["email"]
        }
        user = User(**newUserInfo)
        user.set_password(password)
        user.save()
        return user