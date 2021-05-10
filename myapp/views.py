from django.shortcuts import render
from . import forms
from . import models
from django.shortcuts import redirect

def resume_form(request):
    if request.method == 'GET':
        form_obj = forms.ResumeForm()
        canidate_list = models.Resume.objects.all()
        return render(request, 'myapp/index.html', {'candidates':canidate_list, 'form':form_obj})
    
    if request.method == 'POST':
        form = forms.ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/resume-form/')
        return render(request, 'myapp/index.html', {'form':form})

def resume_details(request, id):
    candidate_details = models.Resume.objects.get(id = id)
    return render(request, 'myapp/candidate_list.html', {'candidate':candidate_details})



