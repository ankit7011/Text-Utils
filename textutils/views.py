#i have created this file -Ankit
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):


    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremover','off')
    ExtraSpaceRemover=request.POST.get('extraspaceremover','off')
    analyzed=djtext;
    purpose=""

    if removepunc=='on':
        analyzed=''
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''

        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        purpose=purpose+' | Remove Punctuations'
        

    if(fullcaps=='on'):
        analyzed=analyzed.upper()
        purpose=purpose+' | Conversion to UPPER CASE '
        params={'purpose':'Conversion to UPPER CASE','analyzed_text':analyzed}
        djtext=analyzed

    if(newlineremove=='on'):
        analyzed=''
        for i in djtext:
            if(i!="\n" and i!='\r'):
                analyzed=analyzed+i
        
        params={'purpose':'New Line Remover','analyzed_text':analyzed}
        
        djtext=analyzed
        purpose=purpose+' | New Line Remover '


    if(ExtraSpaceRemover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        
        params={'purpose':'extraspaceremover','analyzed_text':analyzed}
        djtext=analyzed
        purpose=purpose+' | Extra space remover '

    params={'purpose':purpose,'analyzed_text':analyzed}
    if(ExtraSpaceRemover=='on' or newlineremove=='on' or fullcaps=='on' or removepunc=='on'):
        return render(request,'analyze.html',params)

    else:
        return HttpResponse('Error')

    
    
