from django.contribs.auth.models import User
from rest_framework import permissions
from models import Profile

class IsOwner(permissions.BasePermission):
    #
    message = 'Somente o dono desta conta pode acessar'
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        try:
            user = User.objects.get(user=request.user.id)
            if obj.user == user:
                return True
        except Exception:
            return False