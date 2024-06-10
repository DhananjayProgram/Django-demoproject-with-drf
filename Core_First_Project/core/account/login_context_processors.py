from django.urls import reverse


def login_redirect_context(request):
    should_redirect = request.user.is_authenticated and request.path == reverse('loginuser')
    print(should_redirect)
    return {'should_redirect_from_login': should_redirect}