from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('leads/', include('api.v1.leads.urls')),

]
