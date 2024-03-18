from django.shortcuts import render,redirect

# Create your views here.
from .models import URL
import string
import random
from django.http import HttpResponse


#genera una url 
def generate_url(request):
  if request.method == 'POST':
    long_url=request.POST.get('long_url')
    if long_url == '':
      error_btn="please enter a URL"
      return render(request,'landingPage.html',{'error_btn':error_btn})
    alias=request.POST.get('alias')
    #realizo una busqueda del alias en mi base de datos
    alias_exists=URL.objects.filter(alias=alias).exists() if alias else False
    #si el alias existe en mi base de datos mostrara un error
    if alias_exists:
        error="This alias already , please  write a different one."
        return render (request,'landingPage.html',{'error':error,'long_url':long_url})
    elif len(alias) > 12:
        alias_largo="This alias is too long, please write a shorter alias."
        return render (request,'landingPage.html',{'alias_largo':alias_largo})

    else:
       #si no ingresa ningun alias generara una url aletoria y si lo ingresa mostrara el alias
       character=string.ascii_letters
       short_url=(alias or ''.join(random.choice(character) for i in range(8)))
       #creo un obj en mi bd y se guardara esa url
       obj=URL.objects.create(long_url=long_url,short_url=short_url,alias=alias)
       short_url="https://django-urlshortener-6.onrender.com/" + short_url
       mensaje="Your URL"
       return render(request,'landingPage.html',{'short_url':short_url,'mensaje':mensaje})
  return render(request,'landingPage.html')

def redirect_url(request,short_url):
   try:
      obj=URL.objects.get(short_url=short_url)
   except URL.DoesNotExist:
      obj=None
      return HttpResponse("Error: URL not found")
   if obj is not None:
       obj.save()
       return redirect(obj.long_url)
   else:
       return HttpResponse("error")



