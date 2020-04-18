from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Presentation
from django.core import serializers
from marshmallow import ValidationError
from .validators import PresentationSchema
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import UserProfile
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .serializers import PresentationSerializer

@method_decorator(csrf_exempt, name = 'dispatch')
class ApiView(PermissionRequiredMixin, View):
    http_method_names = ['get', 'post']

    def has_permission(self):
        user = UserProfile.objects.get(user = self.request.user)
        if self.request.method == 'GET':
            return True
        if self.request.method == 'POST' and self.request.user.is_staff:
            return user.token == self.request.headers.get('Authorization')

    def get(self, *args, **kwargs):
        data = serializers.serialize("json", Presentation.objects.all())
        return JsonResponse(data, safe = False)

    def post(self, *args, **kwargs):
        try:
            result = PresentationSchema().load(self.request.POST.dict())
            presentation = Presentation.objects.get(deckId = result['deckId'],
                                                    authorUsername = result['authorUsername'],
                                                    deckSlug = result['deckSlug'])
            return JsonResponse(
                {'url': f'http://slides.com/{presentation.deckSlug}'},
                safe = False, status = 200)
        except ValidationError as err:
            return JsonResponse(err.messages, status = 400)
        except Presentation.DoesNotExist:
            return JsonResponse({'error': 'presentation not found'}, )


class DRFView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = [IsAuthenticated]

    def get(self,request):
        presentations = Presentation.objects.all()
        serializer= PresentationSerializer(presentations,many = True)
        return Response(serializer.data)
    def post(self,request):
        # print(self.request.data)
        result = PresentationSchema().load(self.request.data)
        print(result)

        # presentation = Presentation.objects.get(deckId = result['deckId'],
        #                                         authorUsername = result['authorUsername'],
        #                                         deckSlug = result['deckSlug'])
        # serializer = PresentationSerializer(presentation)
        # return Response(serializer.data)
        return  Response({''})
