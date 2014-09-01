from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.contrib.auth import  logout
from django.http import HttpResponseRedirect 

class IndexAboutView(TemplateView):
    template_name = "base.html"
    

class Privado(View):

	def get(self, request, *args, **kwargs):
		usuario=request.user
		return render(request,'principal/privado.html',{'usuario':usuario})

class Cerrar(View):	

	def get(self, request, *args, **kwargs):
		logout(request)
		return HttpResponseRedirect('/')

