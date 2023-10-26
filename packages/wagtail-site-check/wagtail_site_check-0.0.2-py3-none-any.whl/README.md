# Wagtail Site Check

A Wagtail app to check the configuration of Wagtail Sites.

Have you ever experienced a failing Wagtail preview? Searching for hours, only to find out a misconfiguration of Wagtail Site objects? 
Misconfiguration of hostname and port happens often, goes unnoticed for a while, and leads to vague complaints.

When a Wagtail Site is misconfigured, developers like to be notified. This way, the issue can be addressed quickly. To scratch the itch, I created "Wagtail Site Check".

## Installation

Install the package with pip:

```bash
python -m pip install wagtail-site-check
```

Add the app to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'wagtailsitecheck',
]
```

Add `ALLOWED_WAGTAIL_SITES` to your settings:

```python
ALLOWED_WAGTAIL_SITES = [  
    "a.com:443",
    "b.com:443",
    "c.com:443",
]
```

When working with multiple environments (DTAP), only specify the allowed wagtail sites for that environment. For example via *environment variables*. 

## Usage

The app provides two management commands: `checksites` and `fixsites`.

It also provides a `SiteCheckNotificationPanel` to add a warning to the Wagtail admin dashboard.

### Check Sites

The `checksites` management command *fails hard* if an existing Wagtail Site object is not defined in `ALLOWED_WAGTAIL_SITES`.

``` bash
python manage.py checksites
```

Run this command manually, or add it to your CI/CD pipeline. For example, just after `migrate`.

### Fix Sites

The `fixsites` management command helps to re-configure the sites.

``` bash
python manage.py fixsites
127.0.0.1:8000 is not in ALLOWED_WAGTAIL_SITES. Specify a number to update the site.
  
1: a.com:443
2: b.com:443
3: c.com:443
  
1
  
Updated 127.0.0.1:8000 -> a.com:443
```

### SiteCheckNotificationPanel

To show a warning on the Wagtail admin dashboard add `SiteCheckNotificationPanel` to `wagtail_hooks.py` . The warning is only displayed if there are misconfigured sites.

```python
from wagtail import hooks
from wagtailsitecheck.wagtail_hooks import SiteCheckNotificationPanel

@hooks.register('construct_homepage_panels')
def add_site_check_panel(request, panels):
    panels.append(SiteCheckNotificationPanel())
```
