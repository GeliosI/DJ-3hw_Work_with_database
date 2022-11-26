from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort')

    if sort_param == 'name':
        phones_object = Phone.objects.all().order_by('name')
    elif sort_param == 'min_price':
        phones_object = Phone.objects.all().order_by('price')
    elif sort_param == 'max_price':
        phones_object = Phone.objects.all().order_by('-price')
    else:
        phones_object = Phone.objects.all()

    context = {'phones': phones_object}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone_object}
    return render(request, template, context)
