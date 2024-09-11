import json
import os
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from product.models import Product
from users.models import User
from datetime import datetime


@receiver(post_save, sender=Product)
def post_save_product(sender, instance, created, **kwargs):
    if created:

        subject = 'New product created'
        message = f'{instance.name} product created.'
        from_email = settings.EMAIL_DEFAULT_SENDER
        recipient_list = [user.email for user in User.objects.all()]
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False
        )


@receiver(pre_delete, sender=Product)
def pre_delete_product(sender, instance, **kwargs):

    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(BASE_DIR, 'product\product_data', f'{instance.slug}.json')

    product_data = {
        'id': instance.pk,
        'name': instance.name,
        'description': instance.description,
        'price': instance.price,
        'category': instance.category.id,
        'discount': instance.discount,
        'quantity': instance.quantity
    }

    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    with open(filename, mode='w') as f:
        json.dump(product_data, f, indent=4)

    print('product successfully deleted and saved into file.')
