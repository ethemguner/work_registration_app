#Django Imports
from django.shortcuts import render, HttpResponseRedirect,reverse, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse

#Model & Form Imports
from .forms import RegistryAddingForm
from .models import Registry


def homepage(request):
    return render(request, 'homepage.html')

def list_registry(request):
    registries = Registry.objects.all()

    # Lists.
    notConfirmedList = []
    ConfirmedList = []
    allRegistries = []

    # Seperating confirmed and not confirmed registries.
    for registry in registries:
        if registry.status == "0":
            notConfirmedList.append(registry)
        else:
            ConfirmedList.append(registry)

    # Merge them in a single list. (First not confirmed ones, after confirmed ones.)
    # Therefore, not confirmed registries always be listed first.
    allRegistries = notConfirmedList + ConfirmedList
    return render(request, 'registry/list-registry.html', context={'allRegistries':allRegistries})

def add_registry(request):
    form = RegistryAddingForm(data=request.POST or None)

    if form.is_valid():
        form.save()
        msg = "Registry has added successfully."
        messages.success(request, msg, extra_tags='success')
        return HttpResponseRedirect(reverse('list-registry'))
    return render(request, 'registry/add-registry.html', context={'form':form})

def confirm_registry(request, pk):
    registry = get_object_or_404(Registry, pk=pk)
    registry.status = "1"
    registry.save()
    msg = "Confirmed successfully."
    messages.success(request, msg, extra_tags='success')
    return HttpResponseRedirect(reverse('list-registry'))


def delete_registry(request, pk):
    data ={'is_valid':True}
    registry = get_object_or_404(Registry, pk=pk)
    registry.delete()
    msg = "Deleted successfully."
    messages.success(request, msg, extra_tags='danger')
    return JsonResponse(data=data)