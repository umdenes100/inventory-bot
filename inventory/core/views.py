from django.shortcuts import render
from django.http import HttpResponse

from tabulate import tabulate
import pandas as pd
import json


SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTFcaWz8ylGNayO5HkZBRTuU6fTmGLXLW1NVscDFL0AQvIWU3hbzatm_oZt_J5AyLkT86qizFbyvsNC/pub?output=xlsx'


# Create your views here.
def inventory(request):
    room = int(request.POST['text'].split()[0])

    df = pd.read_excel(SPREADSHEET_URL)
    text = f'*Room:* {room}\n*Status*: All out of everything.\n'
    text += tabulate(df[['Item', room]], tablefmt="pipe", headers="keys")

    data = json.dumps({'text': text})

    return HttpResponse(data, content_type='application/json')
