from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from scrapyd_api import ScrapydAPI
from django_filters.views import FilterView

from .models import Credential, Statement
from .filters import StatementFilterSet

# Create your views here.

scrapyd = ScrapydAPI("http://scrapyd:6800")


class StatementListView(FilterView):
    model = Statement
    ordering = "-tanggal"
    template_name = "statements/list.html"
    filterset_class = StatementFilterSet


statement_list_view = StatementListView.as_view()


@csrf_exempt
@require_http_methods(["POST", "GET"])
def crawl_statement(request):
    if request.method == "POST":
        month_year = request.POST.get("month_year")
        if month_year:
            month, year = month_year.split("/")
        else:
            month, year = None, None

        # TODO: use current user
        bank = request.POST.get("bank_code", "ibmandiri")
        credential = Credential.objects.first()
        task = scrapyd.schedule(
            "default",
            bank,
            month=month,
            year=year,
            userid=credential.userid,
            password=credential.password,
            to_crawl="helloworld"
        )
        return JsonResponse({"task_id": task, "status": "started"})

    task_id = request.GET.get("task_id")
    if not task_id:
        return JsonResponse({"error": "missing task_id argument"})

    status = scrapyd.job_status("default", task_id)
    return JsonResponse({"status": status})
