from django.shortcuts import render

# Create your views here.
def show_form(request):
    """Show the contact form."""
    template_name = "formdata/form.html"
    return render(request, template_name)