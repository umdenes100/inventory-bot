from django.shortcuts import render
from django.http import HttpResponse

import json


# Create your views here.
def inventory(request):
    breakpoint()
    room = request.POST['room']

    data = json.dumps({
        'text': f'*Room:* {room}\nAll out of everything.',
    })

    return HttpResponse(data, content_type='text/plain')
