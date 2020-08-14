from django.urls.conf import path

from .views import BlogView

app_name = 'blogs'

urlpatterns = [
    path('', BlogView.as_view(), name='index'),

]
