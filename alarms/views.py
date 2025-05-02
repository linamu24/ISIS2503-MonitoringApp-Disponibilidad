import random
from django.http import JsonResponse
from django.shortcuts import render

from .logic.logic_alarm import get_alarms, create_alarm

def alarm_list(request):
    alarms = get_alarms()
    context = list(alarms.values())
    return JsonResponse(context, safe=False)

def generate_alarm(request, paciente_id,nombre, tipoSangre, alergias):
    
    #numero entre 1 y 100
    i = random.randint(1, 100)
    if i <= 97:
        alarm = create_alarm(paciente_id, nombre, tipoSangre, alergias)
        return JsonResponse(alarm.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No alarm created'}, status=200)