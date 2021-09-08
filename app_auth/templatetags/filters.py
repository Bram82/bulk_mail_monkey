from django import template

register = template.Library()


@register.filter(name='addclass')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='addPlaceholder')
def add_placeholder(value, args):
    value.field.widget.attrs.update({"placeholder": args})
    return value
