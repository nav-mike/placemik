from webapp.models import CategoryGroup
from theme.forms import NewsletterForm


def categories(_request):
    return {
        "categoryGroups": CategoryGroup.objects.all().prefetch_related("categories"),
        "newsletterForm": NewsletterForm(),
    }
