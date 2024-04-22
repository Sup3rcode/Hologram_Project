
from .models import *


def user_list (request):
    gallery = gallery_Album.objects.all()[:4]
    Article = Articles.objects.all().order_by('-id')[:2]
    vid = Holegram_video.objects.all().last()
    Team = Project_Team.objects.all()
    POverview = Project_Overview.objects.all()
    print(vid)
    context =  {
        'gallery':gallery , 
        'Article':Article , 
        'video':vid , 
        'Team':Team , 
        'POv':POverview , 
        }
    return context