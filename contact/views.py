from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact (request):
    contact_form =ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            content=request.POST.get('content','')   
            # Enviamos el correo y redireccionamos
            email= EmailMessage(
                "La caffeteria: Nuevo mensaje de contacto",                    #asunto
                "De {} <{}> \n\nEscribío:\n\n{}".format(name,email,content),   #Cuerpo
                "carballofernando333@gmail.com",                               #Email de origen
                ["carballofernando333@gmail.com"],                             #Email de destino
                reply_to=[email]                                               #Email de respuesta
            )

            try :
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok" )
            except:
                #algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+" ?fail" )
        
    return render (request,"contact/contact.html",{'form':contact_form})



