# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from userena.decorators import secure_required
from verify.models import VerifyUsers
from verify.forms import AddKeyForm
from userena.utils import user_model_label
@secure_required
@login_required
def changeKey(request):
    user = request.user
#    p = get_object_or_404(user_model_label,user=user)
    try:
        p = VerifyUsers.objects.get(user=user)
    except VerifyUsers.DoesNotExist:
        p = VerifyUsers(user = user)
        p.save()
    if request.method == 'POST':
        form = addKeyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            p.pubkey = data.pubkey
            p.save()
    return render_to_response('verify/changekey.html',{'changeKey':p})