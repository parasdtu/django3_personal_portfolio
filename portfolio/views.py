from django.shortcuts import render
from .models import Info, Contact
from django.contrib import messages

def home(request):
    infos = Info.objects.all()
    return render(request,'portfolio/home.html', {'infos':infos})

def about(request):
    return render(request,'portfolio/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<10 or len(phone)<10 or len(content)<4:
            messages.warning(request, 'Please fill the form correctly ⚠️')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been successfully sent 📨')
    return render(request, 'portfolio/contact.html')
