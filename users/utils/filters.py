from django_filters import rest_framework as filters

from users.models import CustomUser

class UserFilter(filters.FilterSet):
    is_superuser = filters.NumberFilter(field_name='is_superuser', lookup_expr='exact') # NoQa
    is_staff = filters.NumberFilter(field_name='is_staff', lookup_expr='exact')
    is_custom_role_1 = filters.NumberFilter(field_name='is_custom_role_1', lookup_expr='exact') # NoQa
    is_custom_role_2 = filters.NumberFilter(field_name='is_custom_role_2', lookup_expr='exact') # NoQa
    company = filters.CharFilter(field_name='company__company_name', lookup_expr='icontains') # NoQa

    class Meta:
        model = CustomUser
        fields = ['is_superuser', 'is_staff', 'is_custom_role_1', 'is_custom_role_2'] # NoQa
