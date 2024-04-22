from django.shortcuts import render , redirect ,  get_object_or_404,redirect
from .models import *
from .forms import *
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
# Create your views here.
def index(request):
    cache.clear()
    if request.user.is_authenticated:
        pr = User.objects.get(id=request.user.id)
        print(request.user)
        context =  {
            'pr':pr , 
            }
        return render(request, 'Home/index.html', context )
    else:

        return render(request, 'Home/index.html' )




def View_All_Article(request):
    Article = Articles.objects.all()
   
    context =  {
        'Article':Article , 
        }
    return render(request, 'Home/All_Articles.html', context )



class ArticlesDetailView(generic.DetailView):
    model = Articles



@login_required
def Articles_idDetailView(request,Articles_id):
    Articles_pk = get_object_or_404(Articles,pk=Articles_id)
    pr = User.objects.get(id=request.user.id)
    # user = User.objects.first()
    if request.method == "POST":
        form =CommentForm(request.POST)
        if form.is_valid():
            Comments = form.save(commit=False)
            Comments.Articles_id = Articles_pk
            Comments.user = pr
            Comments.save()
            return render(request,'Home/articles_detail.html',{'object':Articles_pk,'form':form})
    else:
        form = CommentForm()

    return render(request,'Home/articles_detail.html',{'object':Articles_pk,'form':form})


def View_All_Gallery(request):
    gallery = gallery_Album.objects.all()
   
    context =  {
        'gallery':gallery , 
        }
    return render(request, 'Home/All_Gallery.html', context )






def View_All_video(request):
    vid = Holegram_video.objects.all()
    
    context =  {
       
        'video':vid , 
       
        
        }
    return render(request, 'Home/All_video.html', context )

