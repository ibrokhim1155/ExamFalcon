import json
import os
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from app.models import Author, Book
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

@receiver(pre_delete, sender=Book)
def save_deleted_book(sender, instance, **kwargs):

    filename = os.path.join(BASE_DIR, 'user/user_data', f'{instance.slug}.json')
    book_data = {
        'id': instance.id,
        'name': instance.name,
        'description': instance.description,
        'author': instance.author.name,
        'published_at': instance.published_at.isoformat() if instance.published_at else None,
        'price': instance.price
    }
    with open(filename, 'w') as f:
        json.dump(book_data, f, indent=4)

@receiver(post_save, sender=Book)
def send_book_email_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Book Added'
        message = render_to_string('emails/new_book_notification.html', {
            'book': instance,
        })
    else:
        subject = 'Book Updated'
        message = render_to_string('emails/book_update_notification.html', {
            'book': instance,
        })

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['recipient@example.com'],
        fail_silently=False
    )
