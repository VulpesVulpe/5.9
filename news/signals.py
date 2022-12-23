from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import *
from .tasks import *



@receiver(m2m_changed, sender=Post.category.through)
def send_mail_on_create_post(sender, action, instance, **kwargs):
    if action == 'post_add':
        cats = instance.category.all()
        for c in cats:
            users = c.subscribers.all()
            for u in users:
                task_send_mail_on_create_post(instance.pk, u.pk)