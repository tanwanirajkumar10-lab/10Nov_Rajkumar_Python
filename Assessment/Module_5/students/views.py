from rest_framework import viewsets
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'message': 'Welcome to EduTracker Solutions API',
        'admin': request.build_absolute_uri('/admin/'),
        'students': reverse('student-list', request=request, format=format),
        'courses': reverse('course-list', request=request, format=format),
    })

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
