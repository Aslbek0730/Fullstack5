from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('app.api.authentication.urls')),
    path('api/courses/', include('app.api.courses.urls')),
    path('api/payments/', include('app.api.payments.urls')),
    path('api/forum/', include('app.api.forum.urls')),
]