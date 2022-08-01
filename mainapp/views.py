from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from mainapp.models import Comment


def index(request):
    context = {
        'page_title': 'Главная',
    }
    return render(request, template_name='mainapp/index.html', context=context)


def comments_page(request):
    comments = Comment.objects.all()
    context = {
        'page_title': 'Отзывы',
        'comments': comments
    }
    return render(request, template_name='mainapp/comments_page.html', context=context)


def comment_page(request, pk, state=0):
    def make_json_response(comment):
        return JsonResponse({
            'url': reverse('main:comment_page', args=(comment.pk, )),
            'description': comment.desc
        })

    comment = Comment.objects.get(pk=pk)
    comment_name = 'comment-text-area'

    if request.method == 'GET' and comment_name in request.GET.keys():
        comment.desc = request.GET[comment_name]
        comment.save()

    if comment.user == request.user and state:
        return make_json_response(comment)
    # return make_json_response(comment)




    context = {
        'page_title': f'Комментарий «{comment.name}»',
        'item': comment,
        'back_url': request.META.get('HTTP_REFERER'),
        'state': state,
    }

    return render(request, template_name='mainapp/comment_page.html', context=context)
