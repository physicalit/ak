from django.contrib import admin
from .models import Slider, Footer, AboutUs, IndexParagraph, Product, ContactSubmission
# Register your models here.
admin.site.register(Slider)
admin.site.register(Footer)
admin.site.register(AboutUs)
admin.site.register(IndexParagraph)
admin.site.register(Product)
@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):

    readonly_fields = ('name', 'email', 'message', 'submitted_at')