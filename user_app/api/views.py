from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from user_app.api.serializers import RegistrationSerializer

# models need to be imported some where for the post_save signal to be executed
from user_app import models


@api_view(['POST'])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def registration_view(request):

    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # the token will be generated after this save function call
            user = serializer.save()

            # create a custom response object to include token
            data = {}
            data['username'] = user.username
            data['email'] = user.email

            data['token'] = Token.objects.get(user=user).key

            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)