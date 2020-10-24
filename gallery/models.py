from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.utils.text import slugify
from PIL import Image
import os


class Category(models.Model):
    title = models.CharField("Kategória név", max_length=200)

    class Meta:
        verbose_name_plural = "Kategóriák"

    def __str__(self):
        return self.title


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField("Cím", max_length=200)
    image = models.ImageField("Kép", upload_to="photos")
    description = models.TextField("Leírás", max_length=2000)
    uploaded = models.DateTimeField(auto_now_add=True)

    slug = models.SlugField(max_length=200, blank=True, editable=False)

    class Meta:
        verbose_name_plural = "Fotók"

    def save(self, *args, **kwargs):
        # if photo is being replaced
        self.replace_image()

        super().save(*args, **kwargs)

        # resize uploaded photo
        self.resize_image()

    def replace_image(self):
        try:
            photo = Photo.objects.get(id=self.id)
            if photo.image.name != self.image.name:
                photo.image.delete(save=False)
        except:
            pass

    def resize_image(self):
        image_path = self.image.path
        img = Image.open(image_path)
        max_size = 1500

        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
            img.save(image_path)

    def __str__(self):
        return self.title


def image_cleanup(sender, instance, **kwargs):
    os.remove(instance.image.path)


post_delete.connect(image_cleanup, sender=Photo)


def slug_generator(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(slug_generator, sender=Photo)