from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, User, SignUpAccess, ContactForm
from .forms import CustomUserCreationForm, AdminCustomUserChangeForm


# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "User Profile"
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = AdminCustomUserChangeForm
    model = User
    list_display_links = ['email']
    search_fields = ['email', 'first_name']
    ordering = ('email', 'is_superuser', 'reg_number')
    filter_horizontal = ()
    inlines = (UserProfileInline,)
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'reg_number', 'user_type', 'first_name', 'last_name',
                           'password', 'date_joined', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', )})
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('email', 'user_type', 'reg_number', 'first_name', 'last_name',
                           'password1', 'password2', 'is_active', 'is_staff', ),
                }
         ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class SignUpAccessAdmin(admin.ModelAdmin):
    search_fields = ['reg_key', 'user_first_name', 'user_email']
    ordering = ('reg_key', 'user_email')
    list_display = ('reg_key', 'user_email', 'is_used')
    list_filter = ('is_used', )


class ContactFormAdmin(admin.ModelAdmin):
    search_fields = ['sender_email', 'sender_full_name']
    ordering = ('sender_email', 'sender_full_name')
    list_display = ('sender_email', 'sender_full_name')


admin.site.register(User, CustomUserAdmin)
admin.site.register(SignUpAccess, SignUpAccessAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
