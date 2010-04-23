from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.core.urlresolvers import reverse

from models import Link
from forms import LinkForm


def user_index(request):
    if request.user.is_authenticated():
        latest_own_links = Link.objects.filter(author=request.user)[:5]
        new_links = Link.objects.exclude(author=request.user).order_by('-created')[:10]
       
        return render_to_response('django_linksharing/user_index.html',
                                    {'user': request.user,
                                     'new_links': new_links,
                                     'latest_own_links': latest_own_links,})
    else:
        return redirect('login/')

@login_required
def user_links(request, username):
    links = Link.objects.filter(author__username=username).order_by('-created')
    return render_to_response('django_linksharing/user_links.html',
                                {'user': request.user,
                                 'url_username': username,
                                 'links': links,})

@csrf_protect
@login_required
def link_add(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
			# We need a custom save method to get the request.user
            Link.objects.create(url=form.cleaned_data['url'],
								description=form.cleaned_data['description'],
								author=request.user)
            return redirect(reverse('django_linksharing.views.user_index'))
        else:
            form = LinkForm(request.POST)
    else:
        form = LinkForm()
    
    return render_to_response('django_linksharing/link_add.html',
                                {'user': request.user,
                                 'form': form,},
                                context_instance=RequestContext(request))

@login_required
def link_detail(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    return render_to_response('django_linksharing/link_detail.html',
                                {'user': request.user,
                                 'link': link,})

@csrf_protect
@login_required
def link_change(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            link.save()
            return redirect(reverse('django_linksharing.views.user_index'))
        else:
            form = LinkForm(request.POST, instance=link)
    else:
        form = LinkForm(instance=link)
    
    return render_to_response('django_linksharing/link_change.html',
                                {'user': request.user,
                                 'form': form,
                                 'link': link,},
                                context_instance=RequestContext(request))
@login_required
def link_index(request):
    return render_to_response('django_linksharing/link_index.html',
                                {'links': Link.objects.order_by('-created'),})
