from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'apiOverview': '/api/v1/',
    }

    return Response(api_urls)
