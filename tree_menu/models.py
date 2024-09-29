from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Menu title")
    slug = models.SlugField(max_length=255, verbose_name="Menu slug")

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    title = models.CharField(max_length=255, verbose_name="Item title")
    url = models.CharField(  # noqa: DJ001
        max_length=255, blank=True, null=True, verbose_name="Item URL"
    )
    named_url = models.CharField(  # noqa: DJ001
        max_length=255, blank=True, null=True, verbose_name="Named URL"
    )
    menu = models.ForeignKey(
        Menu, blank=True, related_name="items", on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        "self", blank=True, null=True, related_name="children", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url if self.url else "#"
