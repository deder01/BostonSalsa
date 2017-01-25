# .. Imports

# Third party
from rest_framework import permissions

# .. End Imports


# Returns true if logged in user owns account being requested
class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False
