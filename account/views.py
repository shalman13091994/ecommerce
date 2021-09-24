from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.db.models.query import InstanceCheckMeta
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from account.models import Address

from .forms import RegistrationForm, UserAddressForm, UserEditForm

# from account.models import UserBase
from .models import Address, Customer
from .token import account_activation_token


@login_required
def dashboard(request):
    return render(request, "account/dashboard/dashboard.html")


def account_register(request):

    if request.method == "POST":
        registerform = RegistrationForm(request.POST)
        if registerform.is_valid():
            user = registerform.save(commit=False)
            #   to prevent the HTML injecting
            user.email = registerform.cleaned_data["email"]
            user.set_password(registerform.cleaned_data["password"])
            #   user won't be active until his email is valid he will get activate email
            user.is_active = False
            user.save()

            # setting up email
            current_site = get_current_site(request)
            subject = "Activate your account"
            message = render_to_string(
                "account/registration/account_activation.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            # from models user is UserBase
            user.email_user(subject=subject, message=message)
            return render(request, "account/registration/register_email_confirm.html", {"form": registerform})

    else:
        registerForm = RegistrationForm()
    return render(request, "account/registration/register.html", {"form": registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        # user = UserBase.objects.get(pk=uid)
        user = Customer.objects.get(pk=uid)

    except ():
        pass
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("account:dashboard")
    else:
        return render(request, "account/registration/activation_invalid.html")


@login_required
def edit_details(request):
# here we haven't used the id because this s the logged in account where the authentication has taken place
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, "account/dashboard/edit_details.html", {"user_form": user_form})


@login_required
def delete_user(request):
    if request.method == "POST":
        # user = UserBase.objects.get(user_name=request.user)
        user = Customer.objects.get(user_name=request.user)
        user.is_active = False
        user.save()
        logout(request)
        return redirect("account:delete_confirmation")


@login_required
def view_address(request):
    addresses = Address.objects.filter(customer=request.user)  # request will have the id
    return render(request, "account/dashboard/addresses.html", {"addresses": addresses})


@login_required
def add_address(request):
    if request.method == "POST":
        address_form = UserAddressForm(data=request.POST)
        if address_form.is_valid():
            address_form = address_form.save(commit=False)
            address_form.customer = request.user
            # request will have the id which should be the same id of the customer
            address_form.save()
            return HttpResponseRedirect(reverse("account:addresses"))

    else:
        address_form = UserAddressForm()
    return render(request, "account/dashboard/edit_addresses.html", {"form": address_form})
    # error- httpresponse return none if we didnt add address_form in the context variable


@login_required
def edit_address(request, id):  # url we have <slud:id> to delete the address of the particular customer id
    if request.method == "POST":
        # we fecthing the details based on the customer id and with the request user
        address = Address.objects.get(pk=id, customer=request.user)
        # instance -- injecting that particular user into the addressform to show the details which they have added before
        address_form = UserAddressForm(instance=address)

        if address_form.is_valid():
            address = Address.objects.get(pk=id)
            address_form = UserAddressForm(instance=address)
            address_form.save()
            return HttpResponseRedirect(reverse("account:addresses"))

    else:
        address = Address.objects.get(pk=id, customer=request.user)
        address_form = UserAddressForm(instance=address)
    return render(request, "account/dashboard/edit_addresses.html", {"form": address_form})


@login_required
def delete_address(request, id):
    address = Address.objects.filter(pk=id, customer=request.user)
    address.delete()
    return redirect("account:addresses")

@login_required
def set_default(request, id):
    # in model default is False
    """"
    we have to find the address which default =True and update it as false
    """
    # WE MAKING THE EXISTING DEFAUKT ADDRESS TO FALSE
    Address.objects.filter(customer=request.user, default=True).update(default=False)
    # now setting up the default address to True
    Address.objects.filter(pk=id, customer=request.user).update(default =True)
    return redirect("account:addresses")
