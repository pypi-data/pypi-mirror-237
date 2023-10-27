
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class Country(models.Model):

    name = models.CharField(_("Country name"), max_length=255)

    flag_logo = models.ImageField(upload_to="countries")

    @property
    def flag_tag(self):
        if not self.flag_logo:
            return ''
        return mark_safe('<img src="%s" title="%s" />' % (
            self.flag_logo.url, self.name
        ))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
