# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from verify.models import VerifyUsers
from Verify.forms import addKeyForm
@secure_required
@login_required
def detail(request):
    user=request.user
    p=get_object_or_404(VerifyUsers,pk=user)
    return render_to_response('verify/detail.html',{'detail':p})
@secure_required
@login_required
def addKey(request):
    user=request.user
    verify_info=VerifyUsers.object.get(user=user)
    if request.method=='POST':
        form=addKeyForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            verify_info.pubkey=data.pubkey
            verify_info.save()
            return HttpResponseRedirect(reverse('verify.views.addKey'))
    render_to_response('verify/addKey.html',{'verfi_info':verify_info})
