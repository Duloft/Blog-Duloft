from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import PostModel

# Create your views here.

def blog_post(request):
    context = {'blogs': PostModel.objects.all()}
    return render(request, 'home.html', context)

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