from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index_boo.html')

    # return HttpResponse("Home")


#def ex1(request):
#    sites = ['''For Entertainment youtube video''',
#             '''For Interaction Facebook''',
#             '''For Insight   Ted Talk''',
#             '''For Internship   Intenship''',
#             ]
#    return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')    # POST ,GET FOR NOT SENDING FULL URL REQUEST
    params = ''
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
           # if char == '\n':
             #   print('\n')
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyze.html', params)
      #  djtext = analyzed
        
    #else:
    #    return HttpResponse("Error")
    if params == '':
        return HttpResponse("Error")
    return render(request,'analyze.html',params)    