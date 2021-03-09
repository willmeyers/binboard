from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, PublicUserSerializer
from .permissions import ActionBasedPermissions, IsStaffOrAdmin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ActionBasedPermissions]

    action_permissions = {
        permissions.AllowAny: ['create', 'retrieve'],
        permissions.IsAuthenticated: ['update', 'partial_update', 'me', 'change_password'],
        IsStaffOrAdmin: ['list', 'destroy']
    }

    @action(detail=False, methods=['get'], name='me')
    def me(self, request):
        user = self.get_serializer(request.user).data

        return Response(user)

    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)

        except User.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

        if user.id != request.user.id:
            return Response(status.HTTP_401_UNAUTHORIZED)

        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        if new_password and confirm_new_password:
            if new_password != confirm_new_password:
                return Response(status.HTTP_400_BAD_REQUEST)    
        
        else:
            return Response(status.HTTP_422_UNPROCESSABLE_ENTITY)
        
        user.set_password(new_password)
        user.save()

        return Response(status.HTTP_202_ACCEPTED)
