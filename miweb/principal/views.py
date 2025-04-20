from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas

class NombreApellidoForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellidos = forms.CharField(label='Apellidos')

def formulario(request):
    if request.method =='POST':
        form = NombreApellidoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellidos = form.cleaned_data['apellidos']

            buffer = BytesIO()
            p = canvas.Canvas(buffer)
            p.drawString(100, 750, f"Hola {nombre} {apellidos}")
            p.showPage()
            p.save()

            buffer.seek(0)
            return HttpResponse(buffer, content_type='application/pdf')
    else:
        form = NombreApellidoForm()
    return render (request, 'formulario.html', {'form': form}) 


    
