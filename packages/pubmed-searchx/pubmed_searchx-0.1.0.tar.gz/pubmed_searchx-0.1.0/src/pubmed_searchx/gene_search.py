from .api import search_pairs_pubmed, get_sum_pubmed_by_ids
from .parser import parse_info_from_summary,parse_ids_from_response
import json
def gene_search(pairs, authors=True, title=True, year=True, pubmed_id=True, path_out=None):
    r"""

    :param pairs: [(gene_name_1, disease_name_1),(gene_name_1, disease_name_1)]

    :param authors: select authors
    :param title: select title
    :param year: select year
    :param pubmed_id: select pubmed_id
    :return:
    """
    info = {}
    is_success = True
    try:
        selectors = {"authors": authors, "title":title, "year":year, "pubmed_id":pubmed_id}
        res, query = search_pairs_pubmed(pairs)
        ids = parse_ids_from_response(res)
        re_sum = get_sum_pubmed_by_ids(ids)
        info = parse_info_from_summary(re_sum, selectors)
    except:
        is_success = False

    if path_out is not None:
        fout = open(path_out, "w")
        fout.write("QUERY: "+ query + "\n")
        if not is_success:
            fout.write("Some error happens, please try again!\n")
        else:
            fout.write(json.dumps(info, indent=2))
        fout.close()
    return info, is_success
