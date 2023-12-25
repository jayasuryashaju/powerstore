# # models.py
# from django.db import models
# from django.core.mail import send_mail
# from django.template.loader import render_to_string

# class Subscriber(models.Model):
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.email

#     def send_thank_you_email(self):
#         subject = 'Thank You for Subscribing!'
#         message = render_to_string('thank_you_email.txt', {'email': self.email})
#         from_email = 'techshopeedjango@gmail.com'  # Replace with your email address
#         to_email = [self.email]

#         send_mail(subject, message, from_email, to_email)
from django.db import models
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

    def send_thank_you_email(self):
        subject = 'Thank You for Subscribing!'
        
        # Render the HTML content
        html_content = render_to_string('thank_you_email.html', {'email': self.email})
        
        # Create a plain text version for email clients that don't support HTML
        text_content = strip_tags(html_content)

        # Set up the email
        msg = EmailMultiAlternatives(subject, text_content, 'powerenough76@gmail.com', [self.email])
        msg.attach_alternative(html_content, "text/html")

        # Send the email
        msg.send()
