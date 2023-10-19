from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from wagtail import hooks


@hooks.register("register_admin_urls")
def register_admin_urls():
    urls = [
        path(
            "jsi18n/",
            JavaScriptCatalog.as_view(packages=["wagtail_publish_test_20231026"]),
            name="javascript_catalog",
        ),
        # Add your other URLs here, and they will appear under `/admin/publish_test_20231026/`
        # Note: you do not need to check for authentication in views added here, Wagtail does this for you!
    ]

    return [
        path(
            "publish_test_20231026/",
            include(
                (urls, "wagtail_publish_test_20231026"),
                namespace="wagtail_publish_test_20231026",
            ),
        )
    ]
