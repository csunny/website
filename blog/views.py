from django.shortcuts import render, redirect
from blog.models import *
from blog.forms import PostForm
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from website.settings import *

# Create your views here.
# article list


def post_list(request):
	posts = Post.objects.all().order_by('-created_date')
	# posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
	#postsall = Post.objects.annotate(num_comment=Count('comment')).filter(published_date_isnull=False).prefetch_related('category').prefetch_related('tags').order_by('-published_date')
	# for p in posts:
	# 	p.click = cache_manager.get_click(p)
	paginator = Paginator(posts, 3)      # show 3 contents per page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# if page is not an integer,deliver first page
		posts = paginator.page(1)
	except EmptyPage:
		# if page is out of range(e.g. 9999),deliver last page of results

		posts = paginator.page(paginator.num_pages)
	return render(request, 'blog/post_list.html', locals())

# article detail


def post_detail(request, pk):
	post = Post.objects.get(id=pk)
	return render(request, 'blog/post_detail.html', locals())

# create new article


@login_required
def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.post_detail', pk=post.id)
	else:
		form = PostForm()

	return render(request, 'blog/post_edit.html', locals())
# edit article


@login_required
def post_edit(request, pk):
    post = Post.objects.get(id = pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


# wait publish
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True). order_by('-created_date')
	return render(request, 'blog/post_draft_list.html', locals())


# article publish function
@login_required
def post_publish(request, pk):
	post = Post.objects.get(id=pk)
	post.publish()
	return redirect('blog.views.post_detail', pk=pk)

# remove article
def post_remove(request, pk):
	post = Post.objects.get(id=pk)
	post.delete()
	return redirect('blog.views.post_list')

# paginate function


