from django.contrib import admin
from .models import Lieferant, Lieferung, Artikel, Lieferposition, Lagerplatz

# Register your models here.


admin.site.register(Lieferant)
admin.site.register(Lieferung)
admin.site.register(Artikel)
admin.site.register(Lieferposition)
admin.site.register(Lagerplatz)