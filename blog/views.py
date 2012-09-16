from django.db.models import Q
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from models import Blog
from forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def searchBlog(request):
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(tag_icontains=query)
        )
        results = Blog.objects.filter(qset).distinct()
    else:
        results = []

    return render_to_response('searchBlog.html', {'results':results , 'query':query})

DEFAULT_MAIL_RECEIVER = 'tonie.tonieh.h@gmail.com'
DEFAULT_MAIL_SENDER = 'your_mail_name@example.com'

@csrf_protect
def contactUs(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            send_mail('feedback for you: %s' % (topic,),
                message,
                sender,
                [DEFAULT_MAIL_RECEIVER],
            )
            return HttpResponseRedirect("")
    else:
        form = ContactForm()
    return render_to_response("contactUs.html",{'form':form},context_instance=RequestContext(request))

def thankU(request):
    return render_to_response("THX.html", {})