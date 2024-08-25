from django.db.models import Q
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from account.serializers import UserSerializer

from .forms import ProjectForm, AttachmentForm
from .models import Project
from .serializers import ProjectSerializer, ProjectDetailSerializer


@api_view(['GET'])
def project_list(request):
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    projects = Project.objects.filter(created_by_id__in=list(user_ids))

    serializer = ProjectSerializer(projects, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def project_detail(request, pk):
    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    project = Project.objects.filter(created_by_id__in=list(user_ids)).get(pk=pk)

    return JsonResponse({
        'Project': ProjectDetailSerializer(project).data
    })


@api_view(['GET'])
def project_list_profile(request, id):   
    user = User.objects.get(pk=id)
    projects = Project.objects.filter(created_by_id=id)

    projects_serializer = ProjectSerializer(projects, many=True)
    user_serializer = UserSerializer(user)

    return JsonResponse({
        'projects': projects_serializer.data,
        'user': user_serializer.data,
    }, safe=False)


@api_view(['project'])
def project_create(request):
    form = ProjectForm(request.project)
    attachment = None
    attachment_form = AttachmentForm(request.project, request.FILES)

    if attachment_form.is_valid():
        attachment = attachment_form.save(commit=False)
        attachment.created_by = request.user
        attachment.save()

    if form.is_valid():
        project = form.save(commit=False)
        project.created_by = request.user
        project.save()

        if attachment:
            project.attachments.add(attachment)

        user = request.user
        user.projects_count = user.projects_count + 1
        user.save()

        serializer = ProjectSerializer(Project)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add somehting here later!...'})


@api_view(['DELETE'])
def project_delete(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    project.delete()

    return JsonResponse({'message': 'Project deleted'})

