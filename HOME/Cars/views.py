from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import transaction

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound

from .models import Car
# Create your views here.

from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import OrderingForm

from Cars.models import Car

class CarList(ListView):
    model = Car
    template_name = 'car_list.html'
    queryset = Car.objects.all().order_by('order')
    context_object_name = 'new_ordering'

class CarView(DetailView):
    model = Car

class CarCreate(CreateView):
    model = Car
    fields = ['name']
    success_url = reverse_lazy('car_list')    

class CarUpdate(UpdateView):
    model = Car
    fields = ['name']
    success_url = reverse_lazy('car_list')

class CarDelete(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')

class CarOrder(ListView):
    model = Car
    success_url = reverse_lazy('car_list')
    
@require_http_methods(["GET","POST"])
def save_new_ordering(request):

    form = OrderingForm(request.POST or None)

    if form.is_valid():
        ordered_ids = form.cleaned_data["ordering"].split(',')

        with transaction.atomic():
            current_order = 1
            for lookup_id in ordered_ids:
                group = Car.objects.get(lookup_id__exact=lookup_id)
                group.order = current_order
                group.save()
                current_order += 1
        return redirect('car_list')

    else:
        return redirect('car_list')





