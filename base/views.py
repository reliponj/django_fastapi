from django.http import HttpResponseRedirect

from base.models import Setting


def settings_view(request):
    settings = Setting.get_settings()
    return HttpResponseRedirect(f'http://{request.META["HTTP_HOST"]}/admin/base/setting/{settings.id}/change/')
