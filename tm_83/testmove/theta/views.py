from django.shortcuts import render
import  requests
import json
from json import dumps

def index(request):
    app_id = '25100167'
    app_key = "6c11d98522ea48b05981ceabef438fa4"
    language = 'en-gb'
    word_id = 'snake'
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
    print(dataJSON)     
    
    return render(request, 'theta/index.html', {'data': dataJSON})
   # print(df)
    # Create your views here.