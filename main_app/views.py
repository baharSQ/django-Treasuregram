from django.shortcuts import render
from .models import Treasure 
from .forms import TreasureForm
from django.http import HttpResponseRedirect
def index(request):
	treasures = Treasure.objects.all()
	form = TreasureForm()
	return render(request, 'index.html', {'treasures':treasures, 'form':form})
def detail (request,treasure_id):
	treasure = Treasure.objects.get(id = treasure_id)
	return render (request, 'detail.html', {'treasure':treasure})
def post_treasure (request):
	form = TreasureForm(request.POST)
	if form.is_valid():
		form.save(commit = True)
#		treasure = Treasure (
#							 name=form.cleaned_data['name'],
#							 value=form.cleaned_data['value'],
#							 material=form.cleaned_data['material'],
#							 location=form.cleaned_data['location'],
#							 img_url= form.cleaned_data['img_url']
#							)
#		treasure.save()
	return HttpResponseRedirect('/')	
#class Treasure:
#	def __init__(self, name, value, material, location):
#		self.name = name
#		self.value = value
#		self.material = material
#		self.location = location
#treasures = [
#	Treasure ('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM"),
#	Treasure ("Fool's Gold",0,'Pyrite',"Fool's Fall, CO"),
#	Treasure ("Cofee Can",20.00,'tin','Acme, CA'),
#]