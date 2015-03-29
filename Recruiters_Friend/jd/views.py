from django.shortcuts import render
from django.http import HttpResponse
import sys
import string_matching 
import json

# Create your views here.
def base(request):
	return render(request,'jd.html')

def rating_calculation(request):
	data=request.POST.get('jd')
	count, absent = string_matching.find_words(data)
	rating=round(float(count)/8*10,1)
	response_data={'rating':rating, 'suggestions':absent}
	return HttpResponse(json.dumps(response_data),content_type="application/json")
