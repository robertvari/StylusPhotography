from django.db import models


class SiteInfo(models.Model):
    site_name = models.CharField("Oldalnév", max_length=200)
    subtitle = models.CharField("Alcím", max_length=200)
    email = models.EmailField("Email", max_length=200, blank=True)
    phone = models.CharField("Telefon", max_length=200, blank=True)

    class Meta:
        verbose_name_plural = "Oldal adatok"

    def __str__(self):
        return self.site_name

