from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Student, Teacher

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
    # the add_fieldsets allowed extra fields to be dispaly on user create form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


class CustomTeacherAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'role']



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher, CustomTeacherAdmin)
admin.site.register(Student)
