from django import template

register = template.Library()



def cut_custom(value, arg):
    """Custom filter: cuts out all values of arg from the input string
    """
    return value.replace(arg, "")


register.filter('cut_custom', cut_custom)

