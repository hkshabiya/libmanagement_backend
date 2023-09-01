from django.contrib import admin
from django import forms

from lib_auth.models import User


# Management
class UserForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        if 'password' in self.changed_data:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdmin(admin.ModelAdmin):
    form = UserForm


admin.site.register(User, UserAdmin)