from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateForm
from django.views import View
from .models import Create


class Create_view(View):
    def get(self, request):
        template_name = 'crud_app/create.html'
        form = CreateForm()
        return render(request, template_name, context={'form': form})

    def post(self, request):
        template_name = 'crud_app/create.html'
        if request.method == 'POST':
            form = CreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('show_url')
        return render(request, template_name, context={'form': form})


class Show_view(View):

    def get(self, request):
        objs = Create.objects.all()
        context = {'objs': objs}
        return render(request, "crud_app/show.html", context)


class Update_view(View):
    def get(self, request, pk):
        obj = Create.objects.get(id=pk)
        form = CreateForm(instance=obj)
        context = {'form': form}
        return render(request, "crud_app/create.html", context)

    def post(self, request, pk):
        obj = Create.objects.get(id=pk)
        form = CreateForm(request.POST, instance=obj)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('show_url')
        return render(request, "crud_app/create.html", context)



class Delete_view(View):
    def get(self, request, pk):
        obj = Create.objects.get(id=pk)
        form = CreateForm(instance=obj)
        context = {'form': form}
        return render(request, "crud_app/confirm.html", context)

    def post(self, request, pk):
        obj = Create.objects.get(id=pk)
        form = CreateForm(request.POST, instance=obj)
        context = {'form': form}
        if request.method == 'POST':
            obj.delete()
            return redirect('show_url')
        return render(request, "crud_app/create.html", context)
