from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth import get_user_model

def image_upload_path(instance, filename):
    '''
    Function that create path for saving item img depends on item slug field.
    '''
    return f"images/{slugify(instance.name)}.png"


class TimestampedModel(models.Model):
    created = models.DateTimeField(
        _('created at'),
        auto_now_add=True,
        blank=True,
    )

    class Meta:
        abstract = True


# Create your models here.
class Beer(TimestampedModel):
    name = models.CharField(
        _('beer name'),
        max_length=255
    )

    description = models.TextField(
        _('beer description')
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

    #relations:
    # user_marks
    # user_comments

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name


class UserMark(TimestampedModel):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        help_text=_('owner of this mark')
    )
    beer = models.ForeignKey(
        'Beer',
        on_delete=models.CASCADE,
        related_name='user_marks',
        help_text=_(
            'shows for which beer this mark is'
        ),
    )
    mark = models.DecimalField(
        _('beer mark'),
        decimal_places=1,
        max_digits=3,
    )

    class Meta:
        ordering = ['-created']
        unique_together = ['owner', 'beer']


class UserComment(TimestampedModel):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        help_text=_('owner of this mark')
    )
    beer = models.ForeignKey(
        'Beer',
        on_delete=models.CASCADE,
        related_name='user_comments',
        help_text=_(
            'shows for which beer this comment is'
        )
    )
    text = models.TextField()

    class Meta:
        ordering = ['-created']
