from operator import concat
from django.shortcuts import render

# Create your views here.
from django.http import BadHeaderError, HttpResponse, request
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
from django.views import generic




from .models import  Contact, Post


def index(request):
    return render(request, 'index.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'pd.html'


from django.shortcuts import render

# Create your views here.

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.lname = lname
        contact.email = email
        contact.message = message
        contact.save()
        
    return render(request, 'contact1.html')