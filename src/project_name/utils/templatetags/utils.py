from django import template
from django.conf import settings
from django.utils.html import format_html

register = template.Library()


class CaptureNode(template.Node):
    def __init__(self, nodelist, var_name):
        self.nodelist = nodelist
        self.var_name = var_name

    def render(self, context):
        output = self.nodelist.render(context)
        context[self.var_name] = output
        return ""


@register.tag
def capture(parser, token):
    """
    Captures contents and assigns them to variable.
    Allows capturing templatetags that don't support "as".

    Example:

        {% templatetag openblock %} capture as body {% templatetag closeblock %}{% templatetag openblock %} lorem 20 w random {% templatetag closeblock %}{% templatetag openblock %} endcapture {% templatetag closeblock %}
        {% templatetag openblock %} include 'components/text/text.html' with body=body only {% templatetag closeblock %}
    """
    args = token.split_contents()
    if len(args) < 3 or args[-2] != "as":
        raise template.TemplateSyntaxError(
            "'capture' tag requires a variable name after keyword 'as'."
        )
    var_name = args[-1]
    nodelist = parser.parse(("endcapture",))
    parser.delete_first_token()
    return CaptureNode(nodelist, var_name)


@register.simple_tag
def placekitten(width=800, height=600):
    """
    Renders a "placekitten" placeholder image.

    Example:

        {% templatetag openblock %}placekitten {% templatetag closeblock %}
        {% templatetag openblock %}placekitten 200 200 {% templatetag closeblock %}
    """
    return format_html('<img src="{}" />'.format(placekitten_src(width, height)))


@register.simple_tag
def placekitten_src(width=800, height=600):
    """
    Return a "placekitten" placeholder image url.

    Example:

        {% templatetag openblock %} placekitten_src as src {% templatetag closeblock %}
        {% templatetag openblock %} placekitten_src 200 200 as mobile_src {% templatetag closeblock %}
        {% templatetag openblock %} include 'components/image/image.html' with mobile_src=mobile_src src=src alt='placekitten' only {% templatetag closeblock %}
    """
    return "//placekitten.com/{}/{}".format(width, height)


@register.simple_tag
def version():
    return settings.RELEASE
