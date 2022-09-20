from django.shortcuts import render

def corona(request):
	return render(request, 'swahili/Coronavirus_ Wafanyakazi wa serikali wapigwa marufuku kusafiri ng’ambo – Taifa Leo.html')

def thika(request):
	return render(request, 'swahili/Wakazi wa Muguga Thika Magharibi wataka usalama uimarishwe – Taifa Leo.html')
	
def serikalini(request):
	return render(request, 'swahili/Wakuu serikalini walaumiwa kwa mauaji nchini – Taifa Leo.html')
