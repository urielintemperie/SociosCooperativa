from django.contrib import admin
from .models import Socio
from .models import Pago
from .models import Importe

# Register your models here.

admin.site.register(Socio)
admin.site.register(Pago)
admin.site.register(Importe)