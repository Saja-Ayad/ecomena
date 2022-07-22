from django.contrib import admin
from .models import Post
#from .models import Contact
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

from django.contrib import admin
from .models import Contact

class contactus(admin.ModelAdmin):
    list_display = ('id','name', 'lname','email','message')
admin.site.register(Contact, contactus )    