import json
import os
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from app.models import Author, Book

@receiver(pre_delete, sender=Book)
def save_deleted_book(sender, instance, **kwargs):
    filename = os.path.join(settings.BASE_DIR, 'app', 'app_data', f'{instance.id}_deleted.json')
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
        message = f'A new book "{instance.name}" by {instance.author.name} has been added.'
    else:
        subject = 'Book Updated'
        message = f'The book "{instance.name}" by {instance.author.name} has been updated.'

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['johnwick@example.com'],
        fail_silently=False
    )
