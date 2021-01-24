from django.shortcuts import render
from projects.models import Project, Comment
from .forms import CommentForm


def home_detail(request):
    return render(request, 'home_detail.html')

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

def contact_detail(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                email=form.cleaned_data["email"],
                subject=form.cleaned_data["subject"],
                body=form.cleaned_data["body"],
            
            )
            comment.save()
    context = {
        "form": form,
    }

    return render(request, 'contact_detail.html',context)