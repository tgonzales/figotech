from django.shortcuts import render_to_response
from django.template import RequestContext

pagename = 'figotech'

def home(request):
    c = {
        'pagename': pagename,
        }

    return render_to_response(
                'index.html', c, context_instance=RequestContext(request))

