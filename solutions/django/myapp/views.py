from django.shortcuts import render
import requests
from myapp.forms import solutionForm
from django.shortcuts import redirect
import json
def home(request):

    if request.session.get("result") != None:
        result = request.session["result"]
    else:
        result = "Hit Enter"
    if request.method == "POST":

        forms = solutionForm(data=request.POST)

        if forms.is_valid():

            url = "http://127.0.0.1:8000/api/v1/"

            x = forms.cleaned_data['x']
            a = forms.cleaned_data['a']
            payload = {'x': x,'a': a}
            files = []
            headers= {}
            response = requests.request("POST", url, headers=headers, data = payload, files = files)
            result = response.json()
            print(result)
            print(type(result))
            request.session["result"] = round(result["result"],5)
            return redirect('myapp:home')
        else:
            pass
    else:
        forms = solutionForm()
    return render(request,"home.html",{"form": forms,"result": result})

    

    



