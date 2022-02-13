from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal info'), {'fields': ('username', 'lastname','date_of_birth','phone', 'gender', 'sinf', 'image')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username', 'lastname','date_of_birth','phone', 'gender', 'sinf', 'image'),
        }),
    )
    list_display = ('name', 'phone', 'sinf', 'is_staff')
    search_fields = ('email', 'username', 'last_name')
    ordering = ('-id',)

    def name(self, ins):
        return ins.username+" "+ins.lastname

    # def group(self, user):
    #     groups = []
    #     for group in user.groups.all():
    #         groups.append(group.name)
    #     return ' '.join(groups)
    # group.short_description = 'Groups'