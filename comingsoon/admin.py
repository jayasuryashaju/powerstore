# admin.py
from django.contrib import admin
from .models import Subscriber
from django.core.mail import send_mail

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)
    actions = ['send_thank_you_email', 'send_notification_email']

    def send_thank_you_email(modeladmin, request, queryset):
        for subscriber in queryset:
            subscriber.send_thank_you_email()
        modeladmin.message_user(request, f'Thank-you email sent to {queryset.count()} subscribers.')

    def send_notification_email(modeladmin, request, queryset):
        subject = 'Website is Live!'
        message = 'Dear subscriber, our website is now live. Thank you for your interest!'
        from_email = 'powerenough76@gmail.com'  # Replace with your email address

        for subscriber in queryset:
            to_email = subscriber.email
            send_mail(subject, message, from_email, [to_email])

        modeladmin.message_user(request, f'Notification email sent to {queryset.count()} subscribers.')

    send_thank_you_email.short_description = 'Send thank-you email to selected subscribers'
    send_notification_email.short_description = 'Send notification email to selected subscribers'

admin.site.register(Subscriber, SubscriberAdmin)
