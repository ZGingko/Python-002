from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed, HttpResponseServerError, HttpResponseRedirect
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg
from django.utils.http import unquote
from django.db.models import Q


from .models import Comments

def index(request):
    return HttpResponseRedirect("/")

class PhoneList(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        key = request.GET.get('q', "")
        keys = None
        conditions = {}
        if key:
            conditions['phone_title__icontains'] = key
            safe = "/#%[]=:;$&()+,!?*@'~"
            keys = []
            for i, k in enumerate(key):
                if k in safe:
                    k = '%{:02X}'.format(ord(k))
                keys.append(k)
            keys = ''.join(keys)

        phone_titles = Comments.objects.values(
            'phone_title').distinct().filter(**conditions)
        template = loader.get_template('phone_list.html')
        context = {'phone_titles': phone_titles, 'keys': keys}
        return HttpResponse(template.render(context))


class PhoneDetail(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        title = unquote(request.GET.get('title', ""))
        name = unquote(request.GET.get('name', ""))
        url = request.get_full_path().split("&name=")[0]
        # print(url)
        # print(unquote(title))
        phone = Comments.objects.filter(Q(phone_title=title), Q(
            comment__icontains=name) | Q(user_name__icontains=name)).order_by('id')
        counter = phone.count()
        user_counter = phone.values('user_name').distinct().count()
        try:
            sent_avg = f" {phone.aggregate(Avg('sentiments'))['sentiments__avg']:0.2f} "
        except:
            sent_avg = 0
        queryset = phone.values('sentiments')
        condtions = {'sentiments__gte': 0.5}
        plus = queryset.filter(**condtions).count()

        queryset = phone.values('sentiments')
        condtions = {'sentiments__lte': 0.5}
        minus = queryset.filter(**condtions).count()

        template = loader.get_template('phone_detail.html')
        return HttpResponse(template.render(locals()))
