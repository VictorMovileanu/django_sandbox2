from django.http import HttpResponse
from .utils import construct_bibtex_query


def bibtex_reference_download(request, item_id: str):
    """

    :param request:
    :param item_id: pure item id, e.g. "item_2632002"
    :return:
    """
    try:
        bibtex_reference = construct_bibtex_query(item_id)
        response = HttpResponse(bibtex_reference, content_type="text/plain")
        response['Content-Disposition'] = 'attachment; filename=bibtex_{}.txt'.format(item_id)
        return response

    except Exception as e:
        print(e)
        return HttpResponse()
