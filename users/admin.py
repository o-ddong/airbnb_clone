from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    User Admin
    - User Model Custom 처리함에 따라 Admin 또한 Customizing
    """
    fieldsets = (
        (
            "Profile",
            {
                "fields": ("username", "password", "name", "email", "is_host"),
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    list_display = ("username", "email", "name", "is_host")