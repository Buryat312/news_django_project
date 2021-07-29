from django.shortcuts import redirect, render, get_object_or_404, reverse

class ObjectCreateMixin:
    form = None
    template = None

    def get(self, request):
        form = self.form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            object = form.save()
            return redirect(object)
        return render(request, self.template, context={'form': form})

class ObjectUpdateMixin:
    form = None
    obj_class = None
    template = None

    def get(self, request, id):
        if not request.user.is_authenticated or request.user.role == 'ordinary':
            return redirect(reverse('post_list_url'))

        obj = get_object_or_404(self.obj_class, id=id)
        bound_form = self.form(instance=obj)
        return render(request, self.template, context={'form': bound_form,
                                                                  self.obj_class.__name__.lower(): obj})

    def post(self, request, id):
        obj = get_object_or_404(self.obj_class, id=id)
        bound_form = self.form(request.POST, instance=obj)
        if bound_form.is_valid():
            obj = bound_form.save()
            return redirect(obj)
        return render(request, self.template, context={'form': bound_form, self.obj_class.__name__.lower(): obj})

class ObjectDeleteMixin:

    obj_class = None
    template = None
    obj_url = None

    def get(self, request, id):
        if not request.user.is_authenticated or request.user.role == 'ordinary':
            return redirect(reverse('post_list_url'))

        obj = get_object_or_404(self.obj_class, id=id)
        return render(request, self.template, context={self.obj_class.__name__.lower(): obj})

    def post(self, request, id):
        obj = get_object_or_404(self.obj_class, id=id)
        obj.delete()
        return redirect(reverse(self.obj_url))
