from django.db import models
from django.db.models.signals import post_delete
from PIL import Image
import os


class SiteInfo(models.Model):
    site_name = models.CharField("Oldalnév", max_length=200)
    logo = models.ImageField("Logo", upload_to="logo", blank=True)
    subtitle = models.CharField("Alcím", max_length=200)
    email = models.EmailField("Email", max_length=200, blank=True)
    phone = models.CharField("Telefon", max_length=200, blank=True)
    
    def save(self, *args, **kwargs):
        # if photo is being replaced
        self.replace_image()

        super(SiteInfo, self).save(*args, **kwargs)

        # resize uploaded photo
        self.resize_image()

    def replace_image(self):
        try:
            site_info = SiteInfo.objects.get(id=self.id)
            if site_info.logo.name != self.logo.name:
                site_info.logo.delete(save=False)
        except:
            pass

    def resize_image(self):
        image_path = self.logo.path
        img = Image.open(image_path)
        max_size = 300

        if img.size[0] > max_size or img.size[1] >max_size:
            img.thumbnail((max_size, max_size))
            img.save(image_path)

    class Meta:
        verbose_name_plural = "Oldal adatok"

    def __str__(self):
        return self.site_name


class About(models.Model):
    title = models.CharField('Címsor', max_length=200)
    content = models.TextField('Üzenet', max_length=5000)

    class Meta:
        verbose_name_plural = "Magunkról"

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField('Cím', max_length=200)
    photo = models.ImageField('Kép', upload_to='services')
    content = models.TextField('Leírás', max_length=5000)

    class Meta:
        verbose_name_plural = "Szolgáltatásaink"

    def save(self, *args, **kwargs):
        # if photo is being replaced
        self.replace_image()

        super(SiteInfo, self).save(*args, **kwargs)

        # resize uploaded photo
        self.resize_image()

    def replace_image(self):
        try:
            service_object = Services.objects.get(id=self.id)
            if service_object.photo.name != self.photo.name:
                service_object.photo.delete(save=False)
        except:
            pass

    def resize_image(self):
        image_path = self.photo.path
        img = Image.open(image_path)
        max_size = 800

        if img.size[0] > max_size or img.size[1] >max_size:
            img.thumbnail((max_size, max_size))
            img.save(image_path)

    def __str__(self):
        return self.title


def logo_cleanup(sender, instance, **kwargs):
    os.remove(instance.logo.path)

post_delete.connect(logo_cleanup, sender=SiteInfo)
