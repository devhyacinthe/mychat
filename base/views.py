from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random 
import time
# Create your views here.

def getToken(request):
    appId = 'ac96eb513ed6439b8dbe36ee2ffa9370'
    appCertificate = 'b12590e3b6c4480b983c01a70d514a49'
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSecond = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTS = currentTimeStamp + expirationTimeInSecond
    role = 1
    
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTS)
    return JsonResponse({'token': token, 'uid': uid}, safe=False)
    
def lobby(request):
    return render(request, 'base/lobby.html')

def room(request):
    return render(request, 'base/room.html')
