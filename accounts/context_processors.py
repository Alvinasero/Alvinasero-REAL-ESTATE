from .permissions import is_site_admin


def site_permissions(request):
    return {
        'can_manage_properties': is_site_admin(request.user),
    }
