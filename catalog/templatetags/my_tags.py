from django import template

register = template.Library()


# @register.filter
# def mediapath(file):
#     return "/media/{{file}}"


@register.simple_tag
def mediapath(file):
    return file.url
