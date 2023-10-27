
from django.contrib import admin

from countries.models import Country


admin.site.register(
    Country,
    list_per_page=100,
    search_fields=['name'],
    list_display=['id', 'name', 'flag_tag']
)
