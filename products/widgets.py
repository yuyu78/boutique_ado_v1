from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
""" Note: Using "as_" means we can now call gettext_lazy() using _()."""

class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/customs_widget_templates/custom_clearable_file_input.html'