from rest_framework import serializers
from ..courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'is_free', 'video_url', 'practical_exercises', 'tests']