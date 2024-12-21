from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def main_page(request):
    return render(request, 'second_task/func_template.html')


class First_page(TemplateView):
    template_name = 'class_template.html'
