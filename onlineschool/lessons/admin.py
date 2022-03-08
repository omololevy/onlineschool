from django.contrib import admin
from .models import (Sinflar, Mavzular, Fanlar, Amaliyot, Maruza)
# Register your models here.

admin.site.register(Sinflar)
admin.site.register(Mavzular)
admin.site.register(Fanlar)
admin.site.register(Amaliyot)
admin.site.register(Maruza)