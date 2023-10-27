Requirements:
```
django-mp-countries
```
Add model field:
```
country = models.ForeignKey(
    "countries.Country",
    models.SET_NULL,
    verbose_name=_("Country"),
    null=True,
    blank=True
)
```
