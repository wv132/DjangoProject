from django.shortcuts import render
from django.http import Http404, HttpResponse
from issueTracker.models import Issue


def index(request):
    tekst = "Hello, Wouter. You're at the issueTracker index."
    latest_issue_list = Issue.objects.order_by('opened_on')[:5]
    context = {'latest_issue_list': latest_issue_list}
    return render(request, 'issueTracker/index.html', context)

def detail(request, issue_id):
    try:
        issue = Issue.objects.get(pk=issue_id)
    except Issue.DoesNotExist:
        raise Http404("Issue does not exist")
    return render(request, 'issueTracker/detail.html', {'issue': issue})    