from django.shortcuts import render, redirect, HttpResponseRedirect

##### ESTEFANO OWO #####
from .bot import chat
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
##### ESTEFANO OWO #####

# Create your views here.

def index(request):
    return render(request, "layouts/index.html")

def get_bot_response(request):
    if request.method == 'GET':
        try:
            user_input = request.GET.get('msg')
            user_input = user_input.lower()

            cadena=""
            for i in user_input:
                if i=="á":
                    i = "a"
                elif i=="é":
                    i = "e"
                elif i=="í":
                    i = "i"
                elif i=="ó":
                    i = "o"
                elif i=="ú":
                    i = "u"

                cadena+=i

            # return HttpResponse(s)

            if cadena:
                print('\n\n==========')
                print(cadena)
                print('==========\n\n')

                while cadena[-1] in "!.":
                    cadena = cadena[:-1]

                msg = chat.respond(cadena)
                return HttpResponse(msg)
            else:
                return HttpResponse("No has dicho nada")
        except Exception as ex:
            return HttpResponse('{"msg":"'+str(ex)+'"}')
