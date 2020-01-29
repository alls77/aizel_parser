from django.contrib import admin

from .models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Price)
