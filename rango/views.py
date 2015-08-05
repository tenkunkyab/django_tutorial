from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template
    context_dict = {'boldmessage': "I am a bold font from the context"}

    # Return a rendered response to send to the client
    # We make use of the shortcut function to make our live easier
    # Note that the first parameter is the the template we wish to use.

    return render(request, '/rango/index.html', context_dict)

