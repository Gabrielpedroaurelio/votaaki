from django.views.generic.edit import CreateView, DeleteView,UpdateView
from .models import PollsModel,PollOptionModel
from django.views.generic.list import ListView
from django.views.generic import TemplateView
# Create your views here.
class IndexView(TemplateView):
    template_name='pages/index.html'
class PollView(ListView):
    model=PollsModel
    template_name='pages/enquete/index.html'
class PollOptionView(ListView):
    model=PollOptionModel
    template_name='pages/vote/index.html'
