# i have created this file - Rahul
from django.http import HttpResponse
from django.shortcuts import render

def links(request):
    l1 = ('''<h1>SSC</h1> <a href="https://ssc.nic.in/">Open SSC website </a>''')
    l2 = ('''<h1>Sarkari Result</h1> <a href="https://sarkariresults.info/"> open sarkariresults from here </a> ''')
    l3 = ('''<h1>You Tube</h1> <a href="https://www.youtube.com/watch?v=sX3L8Lg0TZE&t=161s"> Open Revolt 400 review with Rahul </a>''')
    l4 = ('''<h1>Facebook</h1> <a href="https://www.facebook.com/">Open your facebook account here</a>''')
    l5 = ('''<h1>Instagram</h1> <a href="https://www.instagram.com/">Open your instagram account here</a>''')
    return HttpResponse(f"Navigation Bar: {l1} {l2} {l3} {l4} {l5}")

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove NewLines', 'analyzed_text': analyzed}
        djtext = analyzed


    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed


    if (charcount == "on"):
        analyzed = ""
        analyzed = analyzed + (f"Total character is : {len(djtext)}")
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
            return HttpResponse("please select any operation and try again!!")

    return render(request, 'analyze.html', params)



