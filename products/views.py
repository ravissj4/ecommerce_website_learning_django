from django.shortcuts import render

# Create your views here.
def home(request):
    # context = locals()
    if request.user.is_authenticated():
        # username_is = "Ravi Ranjan"
        # context = {'username_is' : username_is}
        context = {'username_is' : request.user}
    else:
        context = {'username_is' : request.user}
    
    template = 'base.html'
    

    return render(request, template, context)
