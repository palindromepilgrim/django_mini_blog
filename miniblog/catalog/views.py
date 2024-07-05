from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog, Author, Comment
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.
def index(request):
    """View function for home page of site."""
    num_blogs = Blog.objects.all().count()
    num_authors = Author.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    recent_blogs = Blog.objects.all().order_by("-post_date")[:5]
    context = {
        'num_blogs' : num_blogs,
        'num_authors' : num_authors,
        'num_visits' : num_visits,
        'recent_blogs' : recent_blogs
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

class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment_body']

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.user = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog=get_object_or_404(Blog, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated blog.
        """
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'],})