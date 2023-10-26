from unittest.mock import patch

import pytest
from django.core.exceptions import ImproperlyConfigured
from django.core.management import call_command
from wagtail.models import Site

pytestmark = pytest.mark.django_db


def test_check_sites_command():
    with pytest.raises(ImproperlyConfigured) as err:
        call_command("checksites")

    expected = (
        "localhost:80 is not in ALLOWED_WAGTAIL_SITES. "
        "Update via 'Admin -> Settings -> Sites', "
        "or run `fixsites` management command."
    )
    assert expected in str(err.value)


def test_fix_sites_command():
    assert Site.objects.filter(hostname="a.com", port=443).exists() is False
    # The patch completely replaces the input function with a mock object.
    # Therefore, input won't output anything to the console.
    with patch("builtins.input", side_effect="1"):
        call_command("fixsites")
    assert Site.objects.filter(hostname="a.com", port=443).exists() is True
