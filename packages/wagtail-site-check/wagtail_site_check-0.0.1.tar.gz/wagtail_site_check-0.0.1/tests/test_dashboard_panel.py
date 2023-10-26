import pytest
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from pytest_django.asserts import assertInHTML
from wagtail.models import Site

pytestmark = pytest.mark.django_db


def test_dashboard_panel(django_app):
    # Sanity check
    assert Site.objects.count() == 1
    site = Site.objects.first()
    assert site.hostname == "localhost"
    assert site.port == 80

    User = get_user_model()  # noqa: N806
    user = User.objects.create_user(username="admin", is_superuser=True)

    url = reverse("wagtailadmin_home")
    response = django_app.get(url, user=user)
    assert response.status_code == 200
    assert "WARNING: Misconfigured Wagtail Sites" in response
    needle = f'<li>localhost:80 <a href="/admin/sites/{site.id}/">Edit</a></li>'
    assertInHTML(needle, str(response.content, encoding="utf-8"))

    # Fix the site
    site.hostname = "a.com"
    site.port = 443
    site.save()

    response = django_app.get(url, user=user)
    assert response.status_code == 200
    assert "WARNING: Misconfigured Wagtail Sites" not in response
