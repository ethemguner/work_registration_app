from django import template
register = template.Library()

@register.filter
def get_status(i, statusIndex):
    status = "Non-Status"
    if statusIndex == "0":
        status = "Waiting to confirm."
    elif statusIndex == "1":
        status = "Confirmed."
    return status