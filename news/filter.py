from django.forms import DateInput
from django_filters import FilterSet, ModelChoiceFilter, DateFilter

from .models import Post


class PostFilter(FilterSet):
    post_date__gt = DateFilter(widget=DateInput(attrs={'type': 'date'}), field_name='post_date', lookup_expr='gt')
    class Meta:
        model = Post
        fields = {'post_title': ['icontains'], 'post_text': ['icontains']}

