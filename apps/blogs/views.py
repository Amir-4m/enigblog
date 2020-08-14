from django.views.generic import TemplateView
from .models import Post


class BlogView(TemplateView):
    http_method_names = ['get']
    template_name = 'blogs/blog.html'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context.update({'post': Post.objects.first()})
        return context
