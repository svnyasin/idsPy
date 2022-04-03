from django_filters import DateFilter, CharFilter
import django_filters

class PacketFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains", label="Title")

    start_date = DateFilter(field_name="time", lookup_expr="gte", label="Start Date")
    end_date = DateFilter(field_name="time", lookup_expr="lte", label="End Date")

    source = CharFilter(field_name="source", lookup_expr="icontains", label="Source")
    dest = CharFilter(field_name="dest", lookup_expr="icontains", label="Destination")
    proto = CharFilter(field_name="protocol", lookup_expr="icontains", label="Protocol No")
    

    

    content = CharFilter(field_name="p_content", lookup_expr="icontains", label="Content")
    


    