from django.shortcuts import render
from .models import Treasure 
def index(request):
	treasures = Treasure.objects.all()
	return render(request, 'index.html', {'treasures':treasures})
def detail (request,treasure_id):
	treasure = Treasure.objects.get(id = treasure_id)
	return render (request, 'detail.html', {'treasure':treasure})
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