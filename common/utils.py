def is_owner(user, obj):
    return obj.owner == user

def short_text(text, length=50):
    return text[:length] + '...' if len(text) > length else text

from django.shortcuts import redirect

def redirect_back(request, fallback='common:home'):
    return redirect(request.META.get('HTTP_REFERER', fallback))