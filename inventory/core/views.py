from django.shortcuts import render
from django.http import HttpResponse

import json


# Create your views here.
def inventory(request):
    print(request)

    data = json.dumps({
        'type': 'banana',
    })

    return HttpResponse(data, content_type='application/json')
