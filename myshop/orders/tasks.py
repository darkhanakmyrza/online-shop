from celery import task
from django.core.mail import send_mail
from .models import Order
from myshop.settings import EMAIL_HOST_USER


@task
def order_created(order_id):
    """ Oтправки email-уведомлений при успешном оформлении заказа. """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    recepient = str(sub['email'].value())
    message = 'Dear {},\n\n You have succesfully placed an order.\
               You order id is {}.'.format(order.first_name, order.id)
    
    mail_sent = send_mail(subject, 
                          message,
                          EMAIL_HOST_USER, 
                          [order.email])
    return mail_sent