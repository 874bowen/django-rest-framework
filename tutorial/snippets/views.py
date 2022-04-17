from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializerRequest, SnippetSerializerResponse
from django.http import Http404


class SnippetList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializerResponse(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(selfself, request, format=None):
        data = JSONParser().parse(request)  # deserialize
        serializer = SnippetSerializerResponse(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializerResponse(snippet)
        return JsonResponse(serializer.data)

    def put(self, pk, request, format=None):
        snippet = self.get_object(pk)
        data = JSONParser().parse(request)
        serializer = SnippetSerializerRequest(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
