from django.forms.utils import ErrorList
from django.forms.renderers import TemplatesSetting

class CustomFormRenderer(TemplatesSetting):
    form_template_name = 'custom_form_template/bootstrap_template.html'

class BootstrapErrorList(ErrorList):
    template_name = 'form_error/bootstrap_error.html'
    # template_name = 'form_templates/bootstrap_error.html' # doesn't work