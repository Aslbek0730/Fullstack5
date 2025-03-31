from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings
from .serializers import UserSerializer, LoginSerializer
from .tokens import account_activation_token

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        token = account_activation_token.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_link = f"{settings.FRONTEND_URL}/activate/{uid}/{token}/"
        send_mail(
            'Activate Your Account',
            f'Please activate your account by clicking the link: {activation_link}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class ActivateAccountView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, uidb64, token):
        try:
            user = User.objects.get(pk=urlsafe_base64_decode(uidb64).decode())
            if account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                return Response({'message': 'Account activated successfully!'})
            else:
                return Response({'error': 'Activation link is invalid!'}, status=400)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return Response({'error': 'Activation link is invalid!'}, status=400)