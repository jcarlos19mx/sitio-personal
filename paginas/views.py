from django.shortcuts import render
from django.views.generic import TemplateView  # nuevo


def vista_inicio(request):
    contexto = {
        "habilidades": ["Python", "Django", "Git"],
        "mensaje": "GRACIAS por VISITAR mi sitio.",
    }
    return render(request, "inicio.html", contexto)


class VistaAcercaDe(TemplateView):  # nuevo
    template_name = "acerca_de.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["nombre"] = "Ana"
        contexto["edad"] = 20
        return contexto
    
def vista_saludo(request, nombre):  # nuevo
    return render(request, "saludo.html", {"nombre": nombre})