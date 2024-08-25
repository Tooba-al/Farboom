from django.db.models import Q
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions
from .forms import *
from .models import *
from .serializers import *


@api_view(['POST'])
@authentication_classes([])
@permission_classes([permissions.AllowAny])
# def application(request):
#     data = request.data
#     message = 'success'

#     application_form = ApplicationForm(request.POST, request.FILES)
#     if application_form.is_valid():
#         application = application_form.save(commit=False)
#         application.save()
    
#     form = ApplicationForm({
#         'email': data.get('email'),
#         'first_name': data.get('first_name'),
#         'last_name': data.get('last_name'),
#         'education': data.get('education'),
#         'age': data.get('age'),
#         'phone_number': data.get('phone_number'),
#         'cv': data.get('cv'),
#     })

#     if form.is_valid():
#         applicant = form.save()
#         applicant.save()

#     else:
#         message = form.errors.as_json()
    
#     print(message)

#     return JsonResponse({'message': message}, safe=False)
def application(request):
    resume = None
    # resume_form = CreateApplicationForm(request.POST, request.FILES)
    resume_form = ApplicationForm(request.POST, request.FILES)

    if resume_form.is_valid():
        resume = resume_form.save(commit=False)
        resume.created_by = request.user
        resume.save()
        serializer = ResumeSerializer(resume)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add somehting here later!...'})
    

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def resume_list(request):
    # user_ids = [request.user.id]

    # for user in request.user.friends.all():
    #     user_ids.append(user.id)
    # data = request.data
    resumes = Resume.objects.all()

    resumes_serializer = ResumeSerializer(resumes, many=True)

    return JsonResponse({'resumes':resumes_serializer.data},
                        safe=False)

# @api_view(['GET'])
# def resume_detail(request, pk):
#     user_ids = [request.user.id]

#     for user in request.user.friends.all():
#         user_ids.append(user.id)

#     resume = resume.objects.filter(created_by_id__in=list(user_ids)).get(pk=pk)

#     return JsonResponse({
#         'resume': resumeDetailSerializer(resume).data
#     })


# @api_view(['GET'])
# def resume_list_profile(request, id):   
#     user = User.objects.get(pk=id)
#     resumes = resume.objects.filter(created_by_id=id)

#     resumes_serializer = resumeSerializer(resumes, many=True)
#     user_serializer = UserSerializer(user)

#     return JsonResponse({
#         'resumes': resumes_serializer.data,
#         'user': user_serializer.data,
#     }, safe=False)


# @api_view(['resume'])
# def resume_create(request):
#     form = resumeForm(request.resume)
#     application = None
#     application_form = applicationForm(request.resume, request.FILES)

#     if application_form.is_valid():
#         application = application_form.save(commit=False)
#         application.created_by = request.user
#         application.save()

#     if form.is_valid():
#         resume = form.save(commit=False)
#         resume.created_by = request.user
#         resume.save()

#         if application:
#             resume.applications.add(application)

#         user = request.user
#         user.resumes_count = user.resumes_count + 1
#         user.save()

#         serializer = resumeSerializer(resume)

#         return JsonResponse(serializer.data, safe=False)
#     else:
#         return JsonResponse({'error': 'add somehting here later!...'})


@api_view(['DELETE'])
@permission_classes([permissions.AllowAny])
def resume_delete(request, pk):
    resume = Resume.objects.get(pk=pk)
    resume.delete()
    # print(resume)

    return JsonResponse({'message': 'resume deleted'})

