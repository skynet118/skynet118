from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from .models import Course, Order
import json
#from django.template import loader

from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

def simple_checkout(request):
    return render(request, 'payments/simple_checkout.html')

def store(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'payments/store.html', context)

def checkout(request, pk):
    course = Course.objects.get(id=pk)
    context = {'course':course}
    return render(request, 'payments/checkout.html', context)

def payment_complete(request):
    body = json.loads(request.body)
    print('BODY', body)
    course = Course.objects.get(id=body['course_id'])
    Order.objects.create(
            course=course
            )
    return JsonResponse('Payment complete', safe=False)


