from redstat.filters.factory import FilterFactory
from redstat.output.factory import OutputFactory
from redstat.variables.session import BASE_SESSION


def _download(url_template: str, name: str):
    url = url_template.format(name)
    params = {'limit': 100}
    while True:
        response = BASE_SESSION.get(url, params=params)
        response.raise_for_status()

        json_response = response.json()
        data = json_response.get('data')

        children = data.get('children', list())
        for child in children:
            yield child.get('data')

        after = data.get('after', None)
        if after is None:
            break
        params['after'] = after


def get_data(namespace):
    url_template = namespace.url_template
    name = namespace.name
    data = _download(url_template, name)

    filter_class = FilterFactory.get(namespace.filter_type)
    data = filter_class.filter(data, namespace.fields)

    output_class = OutputFactory.get(namespace.output)
    output_class.output(namespace, data)
