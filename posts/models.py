



import itertools
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from django.urls import reverse
from accounts.models import Account
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.text import Truncator
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
import os
from django.core.exceptions import ValidationError
from django.db.models import F


def upload_to(instance, filename):
   # Ensure directory 'media/post/thumbnail', exists
    upload_path = 'post/thumbnails/'
    full_upload_path = os.path.join(upload_path, filename)
    return full_upload_path


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=False, null=False)
    content =RichTextUploadingField(null=False, blank=False, )
    author = models.ForeignKey(Account,on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255, null=True, blank=True, unique=True)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    thumbnail=models.ImageField(upload_to=upload_to,blank=False,null=False)
    name = models.CharField(max_length=128, blank=True)  
    email = models.EmailField(blank=True) 
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    session_id = models.CharField(max_length=255, null=True, blank=True)
    published=models.BooleanField(default=False)

    def get_display_date(self):
        if self.updated and self.updated > self.created:
            return self.updated
        return self.created

    def get_date_label(self):
        if self.updated and self.updated > self.created:
            return 'updated at :'
        return 'posted at :'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            for x in itertools.count(1):
                if not Post.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f'{base_slug}-{x}'

        super(Post, self).save(*args, **kwargs)


    def clean(self):
        super().clean()  

        # Ensure the title is not empty
        if not self.title:
            raise ValidationError("Title field cannot be empty")
         # Ensure thumbnail is either None or has a valid extension
        if self.thumbnail:
            allowed_extensions =['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp',]
            file_extention=os.path.splitext(self.thumbnail.name)[1].lower()
            if file_extention not in  allowed_extensions:
                raise ValidationError(f"  Thumbnail Error : unsuportted  format {file_extention}, allowed extentions are {",".join(allowed_extensions)}")


    def __str__(self):
        if self.author:
            return f"{self.author} posted '{self.title}'"
        else:
            return f"Anonymous post '{self.title}' by {self.name}"
        

    def get_absolute_url(self):
        return reverse("blogpost:post-detail", kwargs={"slug": self.slug})




class PostLikes(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    session_id = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ('user', 'post', 'ip_address', 'session_id')

    def __str__(self):
        if self.user:
            return f"{self.user} likes {self.post}"
        else:
            return f"Anonymous like on {self.post} from IP {self.ip_address}"

class PostComments(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    session_id = models.CharField(max_length=255, null=True, blank=True)
    published=models.BooleanField(default=False)




    def __str__(self):
        if self.user:
            return f"{self.user} commented on {self.post}"
        else:
            return f"Anonymous ({self.name}) commented on {self.post} from IP {self.ip_address}"







@receiver(post_save, sender=PostLikes)
@receiver(post_delete, sender=PostLikes)
def update_post_likes_count(sender, instance, **kwargs):
    if instance.post:
        instance.post.likes_count = PostLikes.objects.filter(post=instance.post).count()
        instance.post.save(update_fields=['likes_count'])



@receiver(post_save, sender=PostComments)
@receiver(post_delete, sender=PostComments)
def update_post_comments_count(sender, instance, **kwargs):
    if instance.post:
        instance.post.comments_count = PostComments.objects.filter(post=instance.post).count()
        instance.post.save(update_fields=['comments_count'])


# models.py
from django.db import models

class DeviceToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token





