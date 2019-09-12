from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Разрешения для администратора
    """
    def has_permission(self, request, view):
        return request.user.is_superuser
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class IsStaff(permissions.BasePermission):
    """
    Разрешения для пользователя с ролью is_staff
    """

    def has_permission(self, request, view):
        return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff


class IsRole_1(permissions.BasePermission):
    """
    Разрешения для пользователя с ролью is_custom_role_1
    """
    def has_permission(self, request, view):
        return request.user.is_custom_role_1

    def has_object_permission(self, request, view, obj):
        return request.user.is_custom_role_1


class IsRole_2(permissions.BasePermission):
    """
    Разрешения для пользователя с ролью is_custom_role_2
    """
    def has_permission(self, request, view):
        return request.user.is_custom_role_2

    def has_object_permission(self, request, view, obj):
        return request.user.is_custom_role_2

