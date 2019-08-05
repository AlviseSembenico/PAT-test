from django.db.models import Q

from ajax_select import register, LookupChannel
from .models import Tool


@register('Tool')
class ToolLookup(LookupChannel):

    model = Tool

    def get_query(self, q, request):
        return self.model.objects.filter(Q(identifier__icontains=q) | Q(name__icontains=q))

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.identifier
