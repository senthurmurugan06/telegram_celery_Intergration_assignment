from django.shortcuts import redirect
from django.views.generic import RedirectView

class APIRootView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return '/api/public/'  # Redirect to your public API endpoint 