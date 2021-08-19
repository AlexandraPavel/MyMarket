from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super().get_queryset()
        user = request.user

        if user.is_superuser:
            return queryset

        return queryset.filter(customer=user)