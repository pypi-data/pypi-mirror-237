from bs4 import BeautifulSoup

def parse_ids_from_response(res, to_string=True):
    res = BeautifulSoup(res, "xml")
    idList = res.IdList
    ids = []
    for ix in idList.find_all("Id"):
        ids.append(ix.text)
    if to_string:
        ids = ",".join(ids)
    return ids

def parse_info_from_summary(sum_res, selectors):
    sum_res = BeautifulSoup(sum_res, "xml" )
    res = []
    for r in sum_res.findAll("DocSum"):
        pubmed_id = r.Id.text
        title = r.findAll('Item', {"Name": "Title"})[0].text
        year = r.findAll('Item', {"Name": "PubDate"})[0].text.split(" ")[0]
        authors_r = r.findAll('Item', {"Name" : "Author"})
        authors = []
        for a in authors_r:
            authors.append(a.text)
        authors = ";".join(authors)
        ri = {"pubmed_id" : pubmed_id, "title": title, "year":year, "authors": authors}
        ro = {}

        for tp, is_selected in selectors.items():
            if is_selected:
                ro[tp] = ri[tp]
        res.append(ri)
    return res