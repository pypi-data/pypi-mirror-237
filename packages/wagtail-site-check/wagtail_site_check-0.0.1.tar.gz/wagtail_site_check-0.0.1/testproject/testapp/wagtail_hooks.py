from wagtail import hooks

from wagtailsitecheck.wagtail_hooks import SiteCheckNotificationPanel


@hooks.register("construct_homepage_panels")
def add_site_check_panel(request, panels):
    panels.append(SiteCheckNotificationPanel())
