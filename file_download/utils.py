import json
import requests


def get_publication_request_data(format='escidoc_snippet'):
    cs = 'https://pure.mpg.de/cone/citation-styles/resource/citation-styles187055'
    return {
        'format': format,
        'citation': 'CSL',
        'cslConeId': cs
    }


def get_bibtex_elastic_search_query(item_id):
    return json.dumps({
        'query': {
            "bool": {
                "must": [
                    {
                        "term": {
                            "publicState": {
                                "value": "RELEASED",
                                "boost": 1.0
                            }
                        }
                    },
                    {
                        "term": {
                            "versionState": {
                                "value": "RELEASED",
                                "boost": 1.0
                            }
                        }
                    },
                    {
                        "bool": {
                            "should": [
                                {
                                    "term": {
                                        "objectId": {
                                            "value": "{}".format(item_id),
                                            "boost": 1.0
                                        }
                                    }
                                },
                                {
                                    "match": {
                                        "objectPid": {
                                            "query": "{}".format(item_id),
                                            "operator": "AND",
                                            "prefix_length": 0,
                                            "max_expansions": 50,
                                            "fuzzy_transpositions": True,
                                            "lenient": False,
                                            "zero_terms_query": "NONE",
                                            "auto_generate_synonyms_phrase_query": True,
                                            "boost": 1.0
                                        }
                                    }
                                },
                                {
                                    "match": {
                                        "versionPid": {
                                            "query": "{}".format(item_id),
                                            "operator": "AND",
                                            "prefix_length": 0,
                                            "max_expansions": 1,
                                            "fuzzy_transpositions": True,
                                            "lenient": False,
                                            "zero_terms_query": "NONE",
                                            "auto_generate_synonyms_phrase_query": True,
                                            "boost": 1.0
                                        }
                                    }
                                },
                                {
                                    "match": {
                                        "metadata.identifiers.id": {
                                            "query": "{}".format(item_id),
                                            "operator": "AND",
                                            "prefix_length": 0,
                                            "max_expansions": 1,
                                            "fuzzy_transpositions": True,
                                            "lenient": False,
                                            "zero_terms_query": "NONE",
                                            "auto_generate_synonyms_phrase_query": True,
                                            "boost": 1.0
                                        }
                                    }
                                },
                                {
                                    "match": {
                                        "metadata.sources.identifiers.id": {
                                            "query": "{}".format(item_id),
                                            "operator": "AND",
                                            "prefix_length": 0,
                                            "max_expansions": 1,
                                            "fuzzy_transpositions": True,
                                            "lenient": False,
                                            "zero_terms_query": "NONE",
                                            "auto_generate_synonyms_phrase_query": True,
                                            "boost": 1.0
                                        }
                                    }
                                }
                            ],
                            "adjust_pure_negative": True,
                            "boost": 1.0
                        }
                    }
                ],
                "adjust_pure_negative": True,
                "boost": 1.0
            }
        }
    })


def construct_bibtex_query(item_id: str) -> bytes:
    """
    Accesses the MPG.PuRe REST API to get the bibtex reference
    :param item_id: e.g. "item_2632002"
    :return:
    """
    response = requests.post(
        'https://pure.mpg.de/rest/items/search',
        params=get_publication_request_data('Nada'),
        # params=get_publication_request_data('BibTex'),
        data=get_bibtex_elastic_search_query(item_id),
        headers={'content-type': 'application/json', 'Cache-Control': 'no-cache'}
    )
    if response.status_code == 200:
        return response.content.decode()
    else:
        raise response.raise_for_status()
