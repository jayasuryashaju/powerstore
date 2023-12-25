from django.http import JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import Subscriber
from .forms import SubscriptionForm

def coming_soon(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')

        # Check if the email is already subscribed
        subscriber, created = Subscriber.objects.get_or_create(email=email)

        if not created:
            # Email is already subscribed, return a response
            return JsonResponse({'message': 'Email is already subscribed!'})

        # Send a thank-you email
        subject = 'Thank You for Subscribing!'
        
        # Use render_to_string to render the HTML content
        message = render_to_string('thank_you_email.html', {'email': email})

        from_email = 'powerenough76@gmail.com'  # Replace with your email address
        to_email = [email]

        # Use the updated send_mail function call
        send_mail(
            subject,
            message,  # Plain text version of the message
            from_email,
            to_email,
            html_message=message,  # HTML version of the message
        )

        return JsonResponse({'message': 'Subscription successful!'})

    form = SubscriptionForm()
    return render(request, 'index.html', {'form': form})
