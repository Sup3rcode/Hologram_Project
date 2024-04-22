from django.db import models
from django.urls import reverse
# Create your models here.
from django.db import models
from users.models import *
from django.conf import settings
# Create your models here.
def Path_Uses_of_holograms(instance,filename):

    return "media/Uses_of_holograms/%s/images.jpeg"%(instance.id )

class Holegram_video(models.Model):
    video_title = models.CharField(max_length=200  )
    link_codes = models.CharField(max_length=200  )
    link_cods = models.CharField(max_length=1000 , blank=True , null=True)
    
    add_by = models.ForeignKey(User,related_name='user_add',on_delete=models.CASCADE , blank=True , null=True)
    add_datet = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.link_codes




class Articles(models.Model):
    title = models.CharField(max_length=225)
    summary = models.TextField()
    content = models.TextField()
    Articles_img=models.FileField(upload_to='media/Article/image/')
    date = models.DateTimeField( auto_now_add=True)
    add_by = models.ForeignKey(User,related_name='user_add_Article',on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = " Articles "

    def __str__(self):
        return str(self.date)
    def get_absolute_url(self):
        return reverse("Home:Home_Articles_detail", args=(self.pk,))
    def get_last_post(self):
        return Comment.objects.filter(Articles_id__id=self.id).all()


class Comment(models.Model):
    user = models.ForeignKey(User,related_name='user_add_Comment',on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    Articles_id = models.ForeignKey(Articles, related_name='Articles_Articles' , on_delete=models.CASCADE)
    Comment_txt = models.TextField()

    def __str__(self):
        return self.Articles_id
    
class gallery_Album(models.Model):
    Name = models.CharField(blank=True,max_length=200 ,null=True)
    image =models.FileField(upload_to='media/Tourism/gallery_Album/')
    date = models.DateTimeField( auto_now_add=True)
    class Meta:
        verbose_name_plural = " gallery_Album"

    def __str__(self):
        return str(self.date)
    



class Project_Team(models.Model):
    Name = models.CharField(max_length=20  )
    Role = models.CharField(max_length=200  )
    About_the_role = models.CharField(max_length=1000 , blank=True , null=True)
    
    def __str__(self):
        return str(self.Name)


class Project_Overview(models.Model):
    Tag = models.CharField(max_length=20  )
    Description = models.TextField(  )
    
    def __str__(self):
        return str(self.Tag)


