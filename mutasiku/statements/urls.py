from django.urls import path
from django.views.generic import TemplateView

from .views import crawl_statement, statement_list_view

app_name = "statements"

urlpatterns = [
    path("list/", statement_list_view, name="list"),
    path(
        "get-statements/",
        TemplateView.as_view(template_name="statements/get_statement.html"),
        name="get_statements",
    ),
    path("crawl/", crawl_statement, name="crawl"),
]
