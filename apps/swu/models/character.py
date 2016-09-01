import logging

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


logger = logging.getLogger(__name__)


class FamilyManager(models.Manager):

    def get_queryset(self):
        return super(FamilyManager, self).get_queryset().all()[:8]


class Character(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='char_images', blank=True)
    height = models.CharField(max_length=20, blank=True)
    mass = models.CharField(max_length=20, blank=True)
    hair_color = models.CharField(max_length=20, blank=True)
    skin_color = models.CharField(max_length=20, blank=True)
    eye_color = models.CharField(max_length=20, blank=True)
    birth_year = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)

    objects = models.Manager()
    family = FamilyManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/character/%i/" % self.id


@receiver(post_save, sender=Character)
def post_save_handler(sender, instance, created, *args, **kwargs):
    action = 'create' if created else 'update'
    do_log(action, instance)


@receiver(post_delete, sender=Character)
def post_delete_handler(sender, instance, *args, **kwargs):
    action = 'delete'
    do_log(action, instance)


def do_log(action, instance):
    msg = '{} | {} | {}'.format(action, instance, instance.id)
    logger.info(msg)
