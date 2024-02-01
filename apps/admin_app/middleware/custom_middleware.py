from django.contrib.auth import get_user


class AdminPanelLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            user = get_user(request)
            if user.is_authenticated:
                request.META['HTTP_ACCEPT_LANGUAGE'] = user.language

        response = self.get_response(request)
        return response
