from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.forms import ContactForms
from blog.models import About,Glas,Best,Abouts
from django.views.generic import ListView


# Create your views here.
def index(request):
    abouts = About.objects.all()
    glass = Glas.objects.all()
    bests = Best.objects.all()
    contact = ContactForms(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2> SO'ROV MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "abouts":abouts,
        "glass":glass,
        "bests":bests
    }
    return render(request,"index.html",context=context)

def about(request):
    aboutss = Abouts.objects.all()
    context = {
        "aboutss":aboutss
    }
    return render(request,"about.html",context=context)

def contact(request):
    contact = ContactForms(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2> SO'ROV MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "contact":contact
    }
    return render(request,"contact.html",context=context)


def shop(request):
    return render(request,"shop.html",context={})

def glasses(request):
    glass = Glas.objects.all()
    context = {
        "glass":glass
    }
    return render(request,"glasses.html",context=context)



def aboutsdetailview(request, abouts):
    about = get_object_or_404(About,slug=abouts)
    context = {
        "about":about
    }
    return render(request,"abouts_Detail.html",context=context)


def glassdetailview(request, glass):
    glas = get_object_or_404(Glas,slug=glass)
    context = {
        "glas":glas
    }
    return render(request,"glass_Detail.html",context=context)

def bestsdetailview(request, bests):
    best = get_object_or_404(Glas,slug=bests)
    context = {
        "best":best
    }
    return render(request,"bests.html",context=context)



def aboutssdetailview(request, aboutss):
    abouts = get_object_or_404(Glas,slug=aboutss)
    context = {
        "abouts":abouts
    }
    return render(request,"aboutss.html",context=context)




class SearchResultsList(ListView):

    model = Glas
    template_name = 'search_result.html'
    context_object_name = 'barcha_kozoynaklar'
    def get_queryset(self):
        query = self.request.GET.get('q')
        print(query)
        return Glas.objects.filter(
            name__icontains=query
        )



















































































































































