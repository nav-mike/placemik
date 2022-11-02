from webapp.models import CategoryGroup


def categories(_request):
    return {
        "categoryGroups": CategoryGroup.objects.all().prefetch_related("categories")
    }
