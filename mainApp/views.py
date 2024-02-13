from django.shortcuts import render
from .models import *
def index(request):
    search = request.GET.get("search")
    togriSozlar = Togri_soz.objects.filter(soz=search)
    if togriSozlar and search:
        togriSoz=togriSozlar[0]
        notogriSozlar = Notogri_soz.objects.filter(togrisoz=togriSoz)
        context = {
            'togriSoz':togriSoz,
            'notogriSozlar':notogriSozlar
        }
        return render(request, 'index.html', context)
    elif search:
        notogriSoz=Notogri_soz.objects.filter(soz=search).first()
        if notogriSoz:
            togriSoz = Togri_soz.objects.get(id=notogriSoz.togrisoz.id)
            notogriSozlar=Notogri_soz.objects.filter(togrisoz=togriSoz)
            context={
                'togriSoz':togriSoz,
                'notogriSozlar':notogriSozlar
            }
        else:
            context = {
                'togriSoz': 'Mavjud emas!',
                'notogriSozlar': ['']
            }
        return render(request, 'index.html', context)
    elif search == '':
        context = {
            'togriSoz': "",
            'notogriSozlar': [""]
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html')

