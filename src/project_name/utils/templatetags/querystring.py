from django import template

register = template.Library()


@register.simple_tag(name='querystring')
def query_string(request, **kwargs):
    """
    Updates a querydict with **kwargs.

    Example::

        {% querystring request foo=bar %}
        {% querystring request key=foo value=bar %}

    NOTE: a QueryDict can normally have the same key name multiple times. Here
    it is forced that a key appears only once, to be used in simple GET searches.

    :param request: The request object.
    :param **kwargs: A dict of to update the request with.
    :return: The updated querystring.
    """
    updated = request.GET.copy()

    key = kwargs.pop('key', None)
    val = kwargs.pop('value', None)

    if key and val:
        updated[key] = val
    else:
        if key in updated:
            del updated[key]
        for k, v in kwargs.items():
            updated[k] = v

    return updated.urlencode()


@register.filter
def getitem(dct, key):
    """
    Simple getter for a ``dict``.

    Example::

        {{ request.GET|getitem:'id' }}  # The key "id".
        {{ request.GET|getitem:id }}  # Variable "id".

    :param dct: The ``dict`` object.
    :param key: The key to find in ``dct``.
    :return: The value belonging to ``key``, or an empty string if the key is not found.
    """
    # import pdb; pdb.set_trace()
    return dct.get(key, '')
