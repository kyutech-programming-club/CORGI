from django.contrib import admin

# Register your models here.

from .models import Valuelec_register
from .models import Lecture
from .models import Teacher

admin.site.register(Valuelec_register)
admin.site.register(Lecture)
admin.site.register(Teacher)
