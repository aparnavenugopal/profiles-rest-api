from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''test api view'''


    def get(self,request,format=None):
        '''returns a list of apiview features'''
        an_apiview=[
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        'is similar to a traditional django view',
        'is mapped manually to urls',
        ]

        return Response({'message':'hello','an_apiview':an_apiview})
