from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from common.decorators import disable_for_loaddata
from accounts.models import Profile

User = get_user_model()


@disable_for_loaddata
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(
            user=instance,
            defaults={
                "user": instance,
            }
        )
