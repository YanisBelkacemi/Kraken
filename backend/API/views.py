from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["get"])
def inputUser(res):
    Inp = {'model' : 'gemma3' , 'prompt' : "why do women hate me ?", 'stream' : False}
    return Response(Inp)
@api_view(["post"])
def Register(res):
    pass

