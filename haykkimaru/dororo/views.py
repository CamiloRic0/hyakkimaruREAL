from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from dororo.form import formularioPartesCuerpo, formularioUbicaciones, formularioDemonios, formularioPeleas, formularioArticulosDororo
from dororo.models import partesCuerpo, Ubicaciones, Resultados, Demonios, Peleas, articulosDororo
from django.http import HttpResponse

# inserts

class insertarPartesCuerpo(generic.CreateView):
    model = partesCuerpo
    template_name = "dororo/formularioPartes.html"
    form_class = formularioPartesCuerpo
    context_object_name = "objPC"
    success_url=reverse_lazy("dororo:Ubicaciones")

class insertarUbicaciones(generic.CreateView):
    model = Ubicaciones
    template_name = "dororo/insertarUbicaciones.html"
    form_class = formularioUbicaciones
    context_object_name = "objU"
    success_url=reverse_lazy("dororo:Demonios")

class insertarDemonios(generic.CreateView):
    model = Demonios
    template_name = "dororo/insertarDemonios.html"
    form_class = formularioDemonios
    context_object_name = "objD"
    success_url=reverse_lazy("dororo:Peleas")

class editarDemonios(generic.UpdateView):
    model = Demonios
    template_name = "dororo/insertarDemonios.html"
    context_object_name = "objD"
    form_class = formularioDemonios
    success_url=reverse_lazy("dororo:Peleas")

class insertarPeleas(generic.CreateView):
    model = Peleas
    template_name = "dororo/insertarPeleas.html"
    form_class = formularioPeleas
    context_object_name = "objP"
    success_url=reverse_lazy("dororo:Articulos")

class insertarArticulosDororo(generic.CreateView):
    model = articulosDororo
    template_name = "dororo/insertarArticulosDororo.html"
    form_class = formularioArticulosDororo
    context_object_name = "objAD"
    success_url=reverse_lazy("dororo:home")

class editarArticulos(generic.UpdateView):
    model = articulosDororo
    template_name = "dororo/editarArticulosDororo.html"
    context_object_name = "objAD"
    form_class = formularioArticulosDororo
    success_url=reverse_lazy("dororo:home")

# lists
class listarFaltantesCuerpo(generic.ListView):
    model = Demonios
    template_name = "dororo/listaFaltantesCuerpo.html"
    context_object_name = "objLSTC"

class listarArticulosDororo(generic.ListView):
    model = articulosDororo
    template_name = "dororo/index.html"
    context_object_name = "objLSTAD"




# delete

class deleteParte (generic.DeleteView):
    model = Demonios
    template_name = "dororo/eliminarDemonio.html"
    context_object_name = "objE"
    success_url=reverse_lazy("dororo:home")

class delete (generic.DeleteView):
    model = articulosDororo
    template_name = "dororo/eliminarArticulo.html"
    context_object_name = "objE"
    success_url=reverse_lazy("dororo:home")

# print

def printArticulos(self, pk=None):
    import io
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import Table

    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    articulosArray = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de articulos de dororo", styles['Heading1'])
    articulosArray.append(header)
    headings = ('id', 'Nombre Articulo', 'Procedencia Articulo', 'castigoDororo')
    # if not pk:
    articulos = [(a.id, a.nombreArticulo, a.procedenciaArticulo, a.castigoDororo)
                           for a in articulosDororo.objects.all().order_by('pk')]
    # else:
    #     todosprofesores = [(p.id, p.nombreParteCuerpo)
    #                        for p in partesCuerpo.objects.filter(id=pk)] 
    
    t = Table([headings] + articulos)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    articulosArray.append(t)
    doc.build(articulosArray)
    response.write(buff.getvalue())
    buff.close()
    return response