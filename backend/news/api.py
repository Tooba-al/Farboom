from django.db.models import Q
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from account.serializers import UserSerializer

from .forms import NewsForm, AttachmentForm
from .models import News
from .serializers import NewsSerializer, NewsDetailSerializer


@api_view(['GET'])
def news_list(request):
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    newss = News.objects.filter(created_by_id__in=list(user_ids))

    serializer = NewsSerializer(newss, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def news_detail(request, pk):
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    news = news.objects.filter(created_by_id__in=list(user_ids)).get(pk=pk)

    return JsonResponse({
        'news': NewsDetailSerializer(news).data
    })


@api_view(['GET'])
def news_list_profile(request, id):   
    user = User.objects.get(pk=id)
    newss = News.objects.filter(created_by_id=id)

    newss_serializer = NewsSerializer(newss, many=True)
    user_serializer = UserSerializer(user)

    return JsonResponse({
        'newss': newss_serializer.data,
        'user': user_serializer.data,
    }, safe=False)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def news_create(request):
    # form = NewsForm(request.POST)
    # attachment = None
    # attachment_form = AttachmentForm(request.POST, request.FILES)

    # if attachment_form.is_valid():
    #     attachment = attachment_form.save(commit=False)
    #     attachment.created_by = request.user
    #     attachment.save()

    # if form.is_valid():
    #     news = form.save(commit=False)
    #     news.created_by = request.user
    #     news.save()

    #     if attachment:
    #         news.attachments.add(attachment)

    #     user = request.user
    #     user.news_count = user.newss_count + 1
    #     user.save()

    #     serializer = NewsSerializer(news)

    #     return JsonResponse(serializer.data, safe=False)
    # else:
    #     return JsonResponse({'error': 'add somehting here later!...'})
    news = None
    # news_form = CreateApplicationForm(request.POST, request.FILES)
    news_form = NewsForm(request.POST, request.FILES)

    if news_form.is_valid():
        news = news_form.save(commit=False)
        # news.created_by = request.user
        news.save()
        serializer = NewsSerializer(news)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add somehting here later!...'})
    

@api_view(['DELETE'])
def news_delete(request, pk):
    news = News.objects.filter(created_by=request.user).get(pk=pk)
    news.delete()

    return JsonResponse({'message': 'news deleted'})

