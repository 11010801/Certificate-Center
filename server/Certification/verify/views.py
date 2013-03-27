# Create your views here.
from django.shortcuts import render_to_response#,get_object_or_404
#from django.http import HttpResponseRedirect,HttpResponse
#from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from userena.decorators import secure_required
from verify.models import VerifyUsers
from verify.forms import AddKeyForm
from userena.utils import user_model_label
@secure_required
@login_required
def changeKey(request):
    user = request.user
    c = {}
    c.update(csrf(request))
#    p = get_object_or_404(user_model_label,user=user)
    try:
        p = VerifyUsers.objects.get(user=user)
    except VerifyUsers.DoesNotExist:
        p = VerifyUsers(user = user)
        p.save()
    if request.method == 'POST':
        form = AddKeyForm(request.POST)
        if form.is_valid():
            pubkey = form.cleaned_data['pubkey']
            p.pubkey = pubkey
            p.save()
    c.update({'changekey':p})
    return render_to_response('verify/changekey.html',c)

from django.http import HttpResponse
def registVerify(request):
    return HttpResponse('registVerify')
    
def verifyUser(request):
    return HttpResponse('verifyUser')

