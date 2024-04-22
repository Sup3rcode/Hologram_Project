from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView , UpdateView
from .forms import *
from .models import *

# Create your views here.

def signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('Home:index')

    return render(request,'users/register.html',{'form':form})

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name','last_name','email',)
    template_name = 'my_account.html'
    success_url = reverse_lazy('Home:index')

    def get_object(self):
        return self.request.user


from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404


class UserProfileView(UpdateView):
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = 'Home:index'
    pk_url_kwarg = "pk"
    def get_object(self): #and you have to override a get_object method
        return get_object_or_404(Profile, user__id=self.request.user.id)
    
from django.views import generic
from django.urls import reverse_lazy
class UserProfileView2(UpdateView):
    template_name = 'users/profile.html'
    model = Profile
    form_class = ProfileForm
    pk_url_kwarg = "pk"
    context_object_name = 'usr'
    success_url = 'Home:index'
    def form_valid(self, form ):
        form.save()
        return redirect('Home:index') 
@login_required
def UserProfileView3(request,board_id):
    #if request.user.is_authenticated:
        
    Profile_pk = get_object_or_404(Profile,id=id)
    usr = get_object_or_404(User,id=request.user.id)
    print(usr)
    
    # user = User.objects.first()
    if request.method == "POST":
        form =ProfileForm(request.POST , request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('board_topics',board_id=Profile_pk.pk)
    else:
        form = ProfileForm()

    return render(request,'users/profile.html',{'usr':Profile_pk,'form':form})

def new_topic(request,usr_id):
    user = get_object_or_404(User,pk=usr_id)
    # user = User.objects.first()
    if request.method == "POST":
        avatar = request.FILES['avatar']
        form =ProfileForm(request.POST , request.FILES)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.avatar = avatar
            topic.save()
            return redirect('users:Update_Profile3',usr_id=request.user.id)
    else:
        form = ProfileForm()

    return render(request,'users/profile.html',{'usr':user,'form':form})

