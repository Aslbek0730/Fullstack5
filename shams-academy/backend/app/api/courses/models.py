from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CourseContent(models.Model):
    course = models.ForeignKey(Course, related_name='contents', on_delete=models.CASCADE)
    video_url = models.URLField()
    exercise_file = models.FileField(upload_to='exercises/')
    test_file = models.FileField(upload_to='tests/')

    def __str__(self):
        return f'Content for {self.course.title}'