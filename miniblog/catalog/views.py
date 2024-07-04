from django.shortcuts import render
from .models import Blog, Author, Comment
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""
    num_blogs = Blog.objects.all().count()
    num_authors = Author.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_blogs' : num_blogs,
        'num_authors' : num_authors,
        'num_visits' : num_visits
    }

    return render(request, 'index.html', context = context)

class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5

class BlogDetailView(generic.DetailView):
    model = Blog

class AuthorDetailView(generic.DetailView):
    model = Author