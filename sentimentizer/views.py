from django.shortcuts import render
from joblib import load

#model = load("c:/users/tonny/desktop/django-stuff/mysite/sentimentizer/model0.joblib")

def analyze(request):
	context = {'sentences':0, 'positives': 0, 'negatives': 0}

	if request.method == 'POST':
		sentiment = request.POST['sentiment']
		lines = sentiment.split(".")
		predictions = [1,1,1,0,0,0,1]#model.predict(lines)
		context['sentences'] = len(lines)
		context['positives'] = len([i for i in predictions if i == 1])
		context['negatives'] = len([i for i in predictions if i == 0])

	return render(request, 'sentimentizer/sentimentizer.html', context)
