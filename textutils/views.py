#I have created this web site -Ayushi
from django.http import HttpResponse
from django.shortcuts import render

def index(requests):
    return render(requests, 'index.html')

def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'remove punctuations', 'analyzed_text':analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to uppercase','analyzed_text':analyzed}
        djtext=analyzed

    if(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if (char != "\n" and char !="\r"):
                analyzed = analyzed + char
        params = {'purpose': 'New line characters removed', 'analyzed_text': analyzed}
        djtext=analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces removed', 'analyzed_text': analyzed}
        djtext=analyzed

    if(removepunc != "on" and fullcaps!="on" and newlineremover!='on' and extraspaceremover!="on"):
        return HttpResponse("please select the an action and try again")

    return render(request, 'analyze.html', params)

