from django.shortcuts import render

def message_list(request):
    return render(request, 'myapp/message_list.html')

