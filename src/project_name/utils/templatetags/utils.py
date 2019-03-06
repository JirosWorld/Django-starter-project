from django import template
from django.utils.html import format_html

register = template.Library()


class CaptureNode(template.Node):
    def __init__(self, nodelist, var_name):
        self.nodelist = nodelist
        self.var_name = var_name

    def render(self, context):
        output = self.nodelist.render(context)
        context[self.var_name] = output
        return ''


@register.tag
def capture(parser, token):
    args = token.split_contents()
    if len(args) < 3 or args[-2] != 'as':
        raise template.TemplateSyntaxError("'capture' tag requires a variable name after keyword 'as'.")
    var_name = args[-1]
    nodelist = parser.parse(('endcapture',))
    parser.delete_first_token()
    return CaptureNode(nodelist, var_name)


@register.simple_tag
def placekitten(width=800, height=600):
    return format_html('<img src="{}" />'.format(placekitten_src(width, height)))


@register.simple_tag
def placekitten_src(width=800, height=600):
    return '//placekitten.com/{}/{}'.format(width, height)
