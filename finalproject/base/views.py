from django.shortcuts import render,HttpResponse,redirect
from base.models import categories,articles
from base.form import RegisterationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django .contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    context={
        'articles':articles.objects.all().filter(status='published',is_trending=True).order_by('updated_at'),
        'articles_not_trending':articles.objects.all().filter(status='published',is_trending=False).order_by('updated_at'),
        }
    return render(request,'main.html',context)


def post_by_category(request,cname):
    category=categories.objects.get(category=cname)

    context={
        'category':cname,
        'articles':articles.objects.all().filter(status='published',category=category.id)
    }
    return render(request,'categories.html',context)



@login_required(login_url='login')
def s_article(request,slug):
    context={
        'article':articles.objects.get(slug=slug)
    }
    return render(request,'article.html',context)


def register(request):
    if request.method=='POST':
       form=RegisterationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('login')
    else:
        form=RegisterationForm()

    
    context={
        'form':form
    }
    return render(request,'register.html',context)



def user_login(request):
    if request.method=='POST':
       form=AuthenticationForm(request,request.POST)
       if form.is_valid():
           username=form.cleaned_data['username']
           password=form.cleaned_data['password']
           user=auth.authenticate(username=username,password=password)
           if user is not None:
               auth.login(request,user)
               return redirect('main')
    else:
       form=AuthenticationForm()
    context={
       'form':form
       
   }
    return render(request,'login.html',context)

def user_logout(request):
    auth.logout(request)
    return redirect('main')
