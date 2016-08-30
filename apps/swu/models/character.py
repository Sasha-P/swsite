from django.db import models


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
