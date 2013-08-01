from django.contrib import admin
from models import *

class BookAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['initial'] = request.user.id
            return db_field.formfield(**kwargs)
        if db_field.name == 'repository':
            latest_book = Book.objects.order_by("-upload_date")
            if len(latest_book) > 0:
                default_repo = latest_book[0].repository.id
                kwargs['initial'] = default_repo
        return super(BookAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

admin.site.register(APIKey)
admin.site.register(Repository)
admin.site.register(Book, BookAdmin)


