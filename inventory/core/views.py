from django.shortcuts import render
from django.http import HttpResponse

import json


# Create your views here.
def inventory(request):
    room = request.POST['text'].split()[0]

    data = json.dumps({
        'text': f'*Room:* {room}\n*Status*: All out of everything.\n',
    })

    return HttpResponse(data, content_type='application/json')
