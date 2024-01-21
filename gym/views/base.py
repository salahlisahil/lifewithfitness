from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from gym.forms import SubscribeForm
from gym.models import TrainingClass, Post
from gym.helpers import subscribe_email


def index(request):
    context = {
        'program_classes': TrainingClass.objects.all(),
        'posts': Post.objects.all()[:5]
    }
    return render(request, 'base/index.html', context=context)


def explore_more(request):
    return render(request, 'base/explore_more.html')


def watch_video(request):
    return render(request, 'base/watchvideo.html')


def weight_lifting(request):
    return render(request, 'base/weight_lifting.html')


def select_plan(request):
    return render(request, 'base/select_plan.html')


def render_post(request):
    posts = Post.objects.all()
    context = {
        'hot_posts': posts[:2],
        'latest_posts': posts[2:],
    }
    return render(request, 'base/blog.html', context=context)


class EmailView(View):
    template_name = 'base/index.html'

    def post(self, request):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            print(321312312)
            try:
                subscribe_email(email=form.cleaned_data.get('email'))
                messages.success(request, 'Thank you for subscribing.')
            except Exception as e:
                messages.error(request, 'Something went wrong while sending email.')

        print(form.errors)

        return redirect('index')

        # return render(request, self.template_name, {'form': form})
