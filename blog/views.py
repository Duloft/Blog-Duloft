# from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import PostModel
from .utils import check_auth_status

# Create your views here.

def home(request):
    access_token = request.COOKIES.get('access_token')
    refresh_token = request.COOKIES.get('refresh_token')
    status, res =  check_auth_status(access_token)
    print(res, 'response')
    if status:
        request.user = res.get('first_name')
    return render(request, 'home.html', )

def features(request):
    return render(request, 'features.html', )

def blog_post(request):
    blogs = PostModel.objects.all().order_by('-created_at')
    paginator = Paginator(blogs, 6)  # Show 6 objects per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) # This is holding both the object and the paginator
    context = {'page_obj': page_obj}
    return render(request, 'blog.html', context)

# @login_required
# def add_blog(request):
 
#     if request.method == 'POST' : # and request.FILES['image']
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             blog_obj = form.save(commit=False)
#             blog_obj.user = request.user
#             # blog_obj.content = content
#             blog_obj.save()
            
#         return redirect('see_blog') 
        
#     else:
#         form = BlogForm()
 
#     context = {'form': form}
#     return render(request, 'add_blog.html', context)

# @login_required
# def blog_update(request, slug):
#     context = {}

#     blog_obj = BlogModel.objects.get(slug=slug)

#     if blog_obj.user != request.user:
#         return redirect('/')

#     initial_dict = blog_obj
#     form = BlogForm(instance=blog_obj)
#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES, instance=blog_obj)

#         if form.is_valid():
#             blog_obj = form.save(commit=False)
#             blog_obj.user = request.user
#             blog_obj.save()

#             return redirect('see_blog')
        
#     context['blog_obj'] = blog_obj
#     context['form'] = form


#     return render(request, 'update_blog.html', context)


def blog_detail(request, slug):
    context = {}
    template_name = 'blog_detail.html'
    
    try:
        blog_obj = get_object_or_404(PostModel, slug=slug)
        context['blog_obj'] = blog_obj
    except Exception as e:
        raise e
    return render(request, template_name, context)

# @login_required
# def see_blog(request):
#     context = {}

#     try:
#         blog_objs = BlogModel.objects.filter(user=request.user)
#         context['blog_objs'] = blog_objs
#     except Exception as e:
#         print(e)

#     print(context)
#     return render(request, 'see_blog.html', context)

# @login_required
# def blog_delete(request, slug):
    # blog_obj = BlogModel.objects.get(slug=slug)
    # print(blog_obj)

    # if blog_obj.user == request.user:
    #     blog_obj.delete()

    # return redirect('/see-blog/')


def pricing(request):
    return render(request, 'pricing.html')

