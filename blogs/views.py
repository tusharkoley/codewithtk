from django.shortcuts import render,  get_object_or_404, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView )

from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.
def blogs( request):
	context = {
	    'posts': Post.objects.all()
	}
	return render (request, "blogs/blogs.html",context)


class PostListView(ListView):
    model = Post
    template_name = 'blogs/blogs.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        
        context['object_list'] = self.model.objects.all()
        context['published_blogs'] = self.model.objects.filter(
            status='Published')
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blogs/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        #slug = self.kwargs["slug"]
       

        comment_form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.filter(active=True)

        context['post'] = post
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comments.filter(active=True)

        context['post'] = post
        context['comments'] = comments
        context['comment_form'] = comment_form
    
        if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
                new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
                new_comment.post = post
#             # Save the comment to the database
                new_comment.save()
        else:
                comment_form = CommentForm()


        return self.render_to_response(context=context)



# def post_detail(request, post):
#     post=get_object_or_404(Post,slug=post,status='published')
#     # List of active comments for this post
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     if request.method == 'POST':
#         # A comment was posted
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#             # redirect to same page and focus on that comment
#             return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
#         else:
#             comment_form = CommentForm()
#     return render(request, 'post_detail.html',{'post':post,'comments': comments,'comment_form':comment_form})


# handling reply, reply view
def reply_page(request):
    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():
            post_id = request.POST.get('post_id')  # from hidden input
            parent_id = request.POST.get('parent')  # from hidden input
            post_url = request.POST.get('post_url')  # from hidden input

            reply = form.save(commit=False)
    
            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()

            return redirect(post_url+'#'+str(reply.id))

    return redirect("/")



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class=PostForm
    # fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class=PostForm
    # fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
