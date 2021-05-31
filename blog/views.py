from django.http import request
from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    if request.session.has_key('blogId'):
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.filter(username = username,password=password).first()
            if user:
                request.session['blogId'] = user.id
                return redirect('home')
            else:
                return render(request,'login.html',{'message':'username or password incorrect'})
        return render(request,'login.html',{})

def register(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST['username']
        user.password = request.POST['password']
        det = Details()
        det.nom = request.POST['nom']
        det.prenom = request.POST['prenom']
        det.img=request.POST['img']
        user.save()
        det.iduser = user
        det.save()
        request.session['blogId'] = user.id
        return redirect('home')
    return render(request,'register.html')

def home(request):
    if request.session.has_key('blogId'):
        list = Article.objects.all()
        return render(request,'article.html',{'list':list})
    else:
        return redirect('login')

def logout(request):
    if not request.session.has_key('blogId'):
        return redirect('login')
    try:
        del request.session['blogId']
        return redirect('login')
    except:
        pass

def addArticle(request):
    if request.session.has_key('blogId'):
        user = User.objects.filter(id = request.session['blogId']).first()
        if request.method == "POST":
            form = Article(iduser = user,title = request.POST['title'],content = request.POST['content'],img = request.FILES['img'])
            print(form.iduser)
            form.save()
            return redirect('home')
        else:
            form = ArticleForm()
            return render(request,'majArticle.html',{'form':form})
    else:
        return redirect('login')
def console(request,id):
    if request.session.has_key('blogId'):
        user = User.objects.filter(id = request.session['blogId']).first()
        det = Details.objects.filter(iduser = id).first()
        article = Article.objects.filter(iduser = id).all()
        profile = 'true'
        
        if user.id == id:
            profile = 'true'
        else:
            proflie = 'false'
        return render(request,'profile.html',{'user':user,'articles':article,'det':det,'profile':profile})

    else:
        return redirect('login')

def delete(request,id):
    if request.session.has_key('blogId'):
        user = User.objects.filter(id = request.session['blogId']).first()
        art = Article.objects.filter(id = id).first()
        art.delete()
        return redirect('home')
    else:
        return redirect('login')

def edit(request,id):
    if request.session.has_key('blogId'):
        user = User.objects.filter(id = request.session['blogId']).first()
        art = Article.objects.filter(id = id).first()
        if request.method == "POST":
            art.title = request.POST['title']
            art.content = request.POST['content']
            
            if request.FILES:
                art.img = request.FILES['img']
            art.save(update_fields=['title','content','img'])
            return redirect('home')
        else:
            return render(request,'editarticle.html',{'art':art})

    else:
        return redirect('login')