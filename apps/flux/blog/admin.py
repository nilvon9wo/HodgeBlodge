from django.contrib import admin
from models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    #exclude = ('create_date',)
    #fields=('title','body_markdown')
    fieldsets = (
        (None, 
             {'fields': (
                  ('title', 'category', 'status'), 
                  'body_markdown', 
                  ('enable_comments'), 
                  'tags', 
                  ('slug')
             )}
        ),
    )
    list_display = ('title', 'enable_comments', 'category', 'status', 'create_date', 'pub_date', 'up_date')
    list_filter = ('enable_comments', 'category', 'status', 'create_date', 'pub_date', 'up_date')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title', 'body_markdown']
    
    def save_model(self,request,obj,form,change):
        if not change:
            obj.author = request.user
        obj.save()




class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
