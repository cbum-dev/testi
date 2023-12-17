from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
@api_view(['GET', 'POST'])
def note(request):

    if request.method == 'GET':
        note = Student.objects.all()
        serializer = StudentSerializer(note, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def note_detail(request, pk):
    try:
        note = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.shortcuts import render
def front(request):
    context = {
        }

    return render(request, "index.html", context)
