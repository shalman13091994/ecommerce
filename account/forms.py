from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.forms.widgets import TextInput

# from .models import
from .models import Address, Customer


class RegistrationForm(forms.ModelForm):
    # modelform -form inputs creating here matching the data fields in the models
    user_name = forms.CharField(label="Enter Username", min_length=4, max_length=50)
    email = forms.EmailField(
        max_length=100, help_text="Required", error_messages={"required": "please enter valid email id"}
    )
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        #   model = UserBase
        model = Customer
        fields = ("user_name", "email")

    def clean_username(self):
        user_name = self.cleaned_data["user_name"].lower()
        r = Customer.objects.filter(user_name=user_name)
        # if the count will have the username as count = 1 like that
        if r.count():
            raise forms.ValidationError("username already exists")
        return user_name

    # def clean_password(self):
    #    cd = self.cleaned_data
    #    if cd['password'] != cd['password2']:
    #       raise forms.ValidationError("'password 'doesn't' match")
    #    return cd['password2']

    def clean_password2(self):
        if (
            "password" in self.cleaned_data
            and "password1" in self.cleaned_data
            and self.cleaned_data["password"] != self.cleaned_data["password1"]
        ):
            raise forms.ValidationError("The password does not match ")
        return self.clean_password2

    def clean_email(self):
        email = self.cleaned_data["email"]
        #   if UserBase.objects.filter(email = email):
        if Customer.objects.filter(email=email):
            raise forms.ValidationError("Email id exist")
        return email

    # for bootstrap - overiding the django forms with the bootstrap
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_name"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Username"})
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "E-mail", "name": "email", "id": "id_email"}
        )
        self.fields["password"].widget.attrs.update({"class": "form-control mb-3", "placeholder": "Password"})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Repeat Password"})


class UserLoginForm(AuthenticationForm):

    # overriding the default login form
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "username", "id": "login_user"})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control mb-3", "placeholder": "password", "id": "login-pwd"})
    )


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label="Account email (can not be changed)",
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "email", "id": "form-email", "readonly": "readonly"}
        ),
    )

    user_name = forms.CharField(
        label="Firstname",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Username",
                "id": "form-firstname",
                "readonly": "readonly",
            }
        ),
    )

    first_name = forms.CharField(
        label="Username",
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={"class": "form-control mb-3", "placeholder": "Firstname", "id": "form-lastname"}
        ),
    )

    class Meta:
        # model = UserBase
        model = Customer
        fields = (
            "email",
            "user_name",
            "first_name",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_name"].required = True
        self.fields["email"].required = True


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.TextInput(attrs={"class": "form-control mb-3", "placeholder": "email", "id": "form-email"}),
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        # u = UserBase.objects.filter(email = email)
        u = Customer.objects.filter(email=email)
        if not u:
            raise forms.ValidationError("email doesnot exist")
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-3", "placeholder": "New Password", "id": "form-newpass"}
        ),
    )
    new_password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control mb-3", "placeholder": "New Password", "id": "form-new-pass2"}
        ),
    )
    # don't need to validate because its auth view django will take care of it


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("full_name", "phone", "address_line", "address_line2", "town_city", "postcode")

    # for bootstrap
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["phone"].widget.attrs.update({"class": "form-control mb-2 account-form", "placeholder": "Phone"})
        self.fields["address_line"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "address_line"}
        )
        self.fields["address_line2"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "address_line"}
        )
        self.fields["town_city"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "town/city"}
        )
        self.fields["postcode"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "postcode"}
        )
