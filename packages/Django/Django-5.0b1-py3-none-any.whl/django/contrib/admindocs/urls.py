from django.contrib.admindocs import views
from django.urls import path, re_path

urlpatterns = [
    path(
        "",
        views.BaseAdminDocsView.as_view(template_name="admin_doc/index.html"),
        name="django-admindocs-docroot",
    ),
    path(
        "bookmarklets/",
        views.BookmarkletsView.as_view(),
        name="django-admindocs-bookmarklets",
    ),
    path(
        "tags/",
        views.TemplateTagIndexView.as_view(),
        name="django-admindocs-tags",
    ),
    path(
        "filters/",
        views.TemplateFilterIndexView.as_view(),
        name="django-admindocs-filters",
    ),
    path(
        "views/",
        views.ViewIndexView.as_view(),
        name="django-admindocs-views-index",
    ),
    path(
        "views/<view>/",
        views.ViewDetailView.as_view(),
        name="django-admindocs-views-detail",
    ),
    path(
        "models/",
        views.ModelIndexView.as_view(),
        name="django-admindocs-models-index",
    ),
    re_path(
        r"^models/(?P<app_label>[^.]+)\.(?P<model_name>[^/]+)/$",
        views.ModelDetailView.as_view(),
        name="django-admindocs-models-detail",
    ),
    path(
        "templates/<path:template>/",
        views.TemplateDetailView.as_view(),
        name="django-admindocs-templates",
    ),
]
