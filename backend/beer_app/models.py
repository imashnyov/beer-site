from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

def image_upload_path(instance, filename):
    '''
    Function that create path for saving item img depends on item slug field.
    '''
    return f"images/{slugify(instance.name)}.png"


# Create your models here.
class Beer(models.Model):
    name = models.CharField(
        _('beer name'),
        max_length=255
    )

    description = models.TextField(
        _('beer description')
    )

    created = models.DateTimeField(
        _('created at'),
        auto_now_add=True,
        blank=True,
    )

    mark = models.DecimalField(
        _('beer mark'),
        decimal_places=1,
        max_digits=3,
    )

    price = models.DecimalField(
        _('beer price'),
        decimal_places=2,
        max_digits=5,
        help_text=_(
            'Beer price in UAH'
        )
    )

    image = models.ImageField(
        _('beer image'),
        upload_to = image_upload_path,
    )

    #marks # user marks to this beer

    #comments # user comments to this beer

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name
