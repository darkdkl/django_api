from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Presentation
from django.core import serializers


@method_decorator(csrf_exempt,name='dispatch')
class ApiView(View):
    http_method_names = ['get','post']
    
    def get(self, *args, **kwargs):
        data = serializers.serialize("json", Presentation.objects.all())
        return JsonResponse(data,safe=False)

    def post(self, *args, **kwargs):       
        deckId=self.request.POST.get('deckId')
        authorUsername=self.request.POST.get('authorUsername')
        deckSlug=self.request.POST.get('deckSlug')        
        if deckId and authorUsername and deckSlug:
            print(deckId, authorUsername, deckSlug)
            try:
                presentation = Presentation.objects.get(deckId = deckId, 
                        authorUsername = authorUsername, deckSlug = deckSlug)                
            except Presentation.DoesNotExist:
                return JsonResponse({'error':'presentation not found'},
                                                                    status=404)
            return JsonResponse(
                        {'url':f'http://slides.com/{presentation.deckSlug}'},
                        safe=False,status=200)
        return JsonResponse({'error':'deckId,authorUsername,deckSlug is required'},
                                                                    status=400)
    