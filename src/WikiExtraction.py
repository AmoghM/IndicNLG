import pandas as pd
import wptools
import json, logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
handler = logging.FileHandler('../logs/TitleUnprocessed.log', 'a+', 'utf-8') # or whatever
handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s')) # or whatever
root_logger.addHandler(handler)

def getWikipedia(title):
    # if index%10 == 0:
    #     print(index)
    try:
        # return {"Name":title}
        wp = wptools.page(title, lang='hi', silent=True)
        return wp.get().data
    except:
        logging.warning(title)
        return {}

def main(titles, index):
    res = []
    print(index)
    for title in titles:
        res.append(getWikipedia(title))
    return res


if __name__ == "__main__":
    # try:
    df = pd.read_csv('../data/hindi_wikibox.tsv', sep='\t')
    titles = df['Title']
    print("CSV uploaded")

    s, e = 0, len(titles)
    for i in range(s, e, 10):

        if i + 10 < e:
            l = i + 10
        else:
            l = len(titles)

        res = main(titles[i:l], i)

        with open("../data/extract/WikiExtract.txt", "a+", encoding='utf-8') as fw:
            for i in res:
                fw.write(str(i)+"\n")
        fw.close()