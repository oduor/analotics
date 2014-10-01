from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import CheckIn, License, Lots
from .forms import CheckInForm

from random import randint
import requests
import time

def get_license_plate(filename):
    print filename
    files = {'lpimage': open(filename, 'rb')}
    nonce = str(randint(1, 900000000))
    d = {'nonce': nonce}
    requests.post("http://demo.openalpr.com:8010/upload", files=files, data=d)
    print("Processing...")
    job_status = 0
    while job_status != 3 and job_status != 4:
        time.sleep(0.1)
        r2 = requests.get("http://demo.openalpr.com:8010/status?nonce={0}".format(nonce))
        r2s = r2.json()
        job_status = r2s['job_status']
        if job_status == 3:
            plates = [(x['plate'], x['confidence']) for x in r2s['plates']]
            if plates:
                return sorted(plates, key=lambda x: x[1])[-1][0]

def checkin(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST, request.FILES)
        license_file = request.FILES['licensefile']
        with open('/tmp/license-checkin.jpg', 'wb+') as destination:
                for chunk in license_file.chunks():
                    destination.write(chunk)
        license_number = get_license_plate('/tmp/license-checkin.jpg')
        if license_number:
            license = License(plate=license_number)
            license.save()
        return HttpResponseRedirect('/licenses/')
    else:
        lots = Lots.objects.all()
        context = RequestContext(request, {'lots': lots})
        return render_to_response('checkin.html', context)

def lots(request):
    lots = Lots.objects.all()
    context = RequestContext(request, {'lots': lots})
    return render_to_response('visualization.html', context)


def licenses(request):
    licenses = License.objects.all()
    context = RequestContext(request, {'licenses': licenses})
    return render_to_response('licenses.html', context)
