from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
# from basket module inside basket.py importing Basket class
from basket.basket import Basket
from orders.views import payment_confirmation


@login_required
def BasketView(request):

    # we will take information from session which is in basket class where we will get basket session 
   """
   when user goes to basket page we gonna take all the information from the basket session
   """  
   basket = Basket(request) 
   total = str(basket.get_total_price())
#we can't send in decimal to stripe so we replacing "." with "" 
   total = total.replace('.', '')
   total = int(total) 

   print(total)

#stripe api secret key available under developers-->api
   stripe.api_key = 'sk_test_51JU92jSIhpZR8wXzajV7kQOUIwJLeqTOQCCts989MB36MOGCpTCqMHuizU1gFtt1hSPbC0Hlf0eY9OK2M3krOrWR00Kpz1KPF6'
 # setting up intent to send (created)
   intent = stripe.PaymentIntent.create(
       amount = total,
       currency = 'INR',
       metadata = {'userid' : request.user.id}
    # will take this id and save it to database so that we can know who has done the payment
   )
# receiving intent as client_secret key 
   return render(request, "payment/payment_form.html", {'client_secret':intent.client_secret})

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.client_secret)

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)


   # order placed
def order_placed(request):
   basket = Basket(request)
   basket.clear() #we want to clear the basket make it zero after the payment 
   return render(request, 'payment/order_placed.html')