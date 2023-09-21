from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
from csv import DictReader
from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    bus_station = []
    page_number = int(request.GET.get("page", 1))
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_station.append(row)
    paginator = Paginator(bus_station, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
