from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
import  requests
import json
from json import dumps


tasks = ["foo", "bar", "baz"]






class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Synonym")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]            
            
            #request.session["tasks"] += [task]
            
            request.session["tasks"] = [task]


            app_id = '25100167'
            app_key = "6c11d98522ea48b05981ceabef438fa4"
            language = 'en-gb'
            word_id = task
            url = 'https://od-api.oxforddictionaries.com/api/v2/thesaurus/'  + language + '/'  + word_id.lower()

            api_results = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

            frm_api = json.loads(api_results.text)

            rslts = frm_api['results']

            ntrys = rslts[0]['lexicalEntries'][0]


            etym = ntrys['entries'][0]

            sns = etym['senses']

            df = sns[0
                    ]
            df['synonyms']
            #dataJSON = dumps(df)
    
            dataJSON = dumps(frm_api)
    

            
            
            # return render(request, "tasks/add.html")         
        
            #return HttpResponseRedirect(reverse("tasks:index"))
####################################################################################

            return render(request, "tasks/mod.html", {

###################################################################################

                "syn": task, "word" : dataJSON
            })


        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    else:
        return render(request, "tasks/add.html", {
            "form": NewTaskForm()
        })


# Add a new task:


        
def prcs(request):
     return render(request, "tasks/prcs.html")


def mod(request):
     return render(request, "tasks/mod.html")

            
