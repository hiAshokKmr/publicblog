





from django.contrib import admin

from accounts.models import Account

from .models import *



admin.site.register(Category)
admin.site.register(Language)

class PostLikesInline(admin.TabularInline):
    model = PostLikes
    extra = 1


class PostCommentsInline(admin.TabularInline):
    model = PostComments
    fields=['published','text','user','name','email','ip_address','session_id']
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model=Post
    # form = PostForm
    list_display = ['id', 'title','category', 'language','published']
    list_display_links = ['title']
    search_fields = ['id','title', 'author__username', 'author__email','slug']
    readonly_fields = ['created', 'updated', 'likes_count', 'comments_count','slug']
    inlines = [PostLikesInline, PostCommentsInline]
    

    # #to show only admins and staffs in post author field.
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "author":
    #         kwargs["queryset"] = Account.objects.filter(is_staff=True)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    #search by
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term.lower() in ['true', 'false']:
            bool_value = search_term.lower() == 'true'
            queryset |= self.model.objects.filter(user__is_admin=bool_value)
            queryset |= self.model.objects.filter(user__is_staff=bool_value)
            queryset |= self.model.objects.filter(user__is_whitelisted=bool_value)
            queryset |= self.model.objects.filter(user__is_superuser=bool_value)
        return queryset, use_distinct


admin.site.register(Post, PostAdmin)



class PostLikesAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'post']

    search_fields = ['user__username', 'user__email', 'post__title']


admin.site.register(PostLikes, PostLikesAdmin)



class PostCommentsAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'post', 'created']
    search_fields = ['user__username', 'user__email', 'post__title', 'text'] 

admin.site.register(PostComments, PostCommentsAdmin)


admin.site.register(DeviceToken)
