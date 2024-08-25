from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import *
from .models import *
from .serializers import *


@api_view(['GET'])
# @permission_classes([])
# @authentication_classes([])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
    })


@api_view(['GET'])
@permission_classes([])
def users_list(request):
    users = User.objects.all()

    user_serializer = UserSerializer(users, many=True)

    return JsonResponse({'users':user_serializer.data},
                        safe=False)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def profile(request):
    return JsonResponse({
        'id': request.user.id,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
    })


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'first_name': data.get('first_name'),
        'last_name': data.get('last_name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    # try:
    #     user = form.save()
    #     user.save()
    # except:
    #     message = "couldn't save the user information."
    
    if form.is_valid():
        user = form.save()
        user.is_active = False
        user.save()

        # url = f'{settings.WEBSITE_URL}/activateemail/?email={user.email}&id={user.id}'

        # send_mail(
        #     "Please verify your email",
        #     f"The url for activating your account is: {url}",
        #     "noreply@wey.com",
        #     [user.email],
        #     fail_silently=False,
        # )
    else:
        message = form.errors.as_json()
    
    print(message)

    return JsonResponse({'message': message}, safe=False)


@api_view(['POST'])
def editprofile(request):
    user = request.user
    email = request.data.get('email')

    if User.objects.exclude(id=user.id).filter(email=email).exists():
        return JsonResponse({'message': 'email already exists'})
    else:
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
        # form.save()
        
        serializer = UserSerializer(user)

        return JsonResponse({'message': 'information updated', 'user': serializer.data})
    

@api_view(['POST'])
def editpassword(request):
    user = request.user
    
    form = PasswordChangeForm(data=request.POST, user=user)

    # try:
    #     form.save()
    #     return JsonResponse({'message': 'success'})
    # except:
    #     return JsonResponse({'message': form.errors.as_json()}, safe=False)
    
    if form.is_valid():
        form.save()

        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': form.errors.as_json()}, safe=False)


