import json
from django.http import HttpResponse

def main(request):

    msg = {"message" : "Hello World!"}
    JSON = json.dumps(msg)
    
    return HttpResponse(JSON)
