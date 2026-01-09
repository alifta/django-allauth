from allauth.account import app_settings
from allauth.account.views import SignupView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods, require_POST

from core.forms import TodoForm
from core.models import Todo, Transaction


def index(request):
    context = {}
    return render(request, "core/index.html", context)


def about(request):
    context = {}
    return render(request, "core/partials/about.html", context)


@login_required
def secret(request):
    return render(request, "core/secret.html")


@login_required
def todo(request):
    context = {
        "todos": Todo.objects.filter(user=request.user),
        "form": TodoForm(),
    }
    return render(request, "core/todo.html", context)


def transactions(request):
    count = Transaction.objects.count()
    context = {"count": count}
    return render(request, "core/transactions.html", context)


@login_required
@require_POST
def submit_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()

        # Return the partial HTML for the new todo item
        context = {"todo": todo}
        return render(request, "core/todo.html#todo-item-partial", context)


@login_required
@require_POST
def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.is_completed = True
    todo.save()
    context = {"todo": todo}
    return render(request, "core/todo.html#todo-item-partial", context)


@login_required
@require_http_methods(["DELETE"])
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    response = HttpResponse(status=204)
    response["HX-Trigger"] = "delete-todo"
    return response


class CustomSignupView(SignupView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["custom_message"] = (
            "Join 10,0000+ visionary realestate community using out cutting-edge, AI-powered, blockchain-enabled, cloud-native platform to disrupt the paradigm and synergize realestate investing!"
        )

        return context

    def form_valid(self, form):
        # Add any custom logic here before saving the user
        response = super().form_valid(form)

        if (
            app_settings.EMAIL_VERIFICATION
            == app_settings.EmailVerificationMethod.MANDATORY
        ):
            messages.info(
                self.request,
                "Please verify your email address to complete the registration.",
            )
        else:
            messages.success(
                self.request,
                f"Welcome {form.cleaned_data.get('first_name', '')}! You have signed up successfully.",
            )

        return response
