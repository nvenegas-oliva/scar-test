from textanalyzer.Corpus import Corpus

def lambda_handler(event, context):
    corpus = Corpus()
    for d in event:
        corpus.add_doc(d)
    results = []
    corpus.clean(stopwords=True,
                lower=False,
                clean_vowels=True,
                remove_numbers=True)
    for d in corpus.docs:
        results.append(corpus.docs[d].trans)
    return {'results' : results}

if __name__ == '__main__':
    ## Load data for test
    url_dataset = "data.txt"
    data = [line.strip() for line in open(url_dataset, 'r')]
    ## Use module
    #corpus = Corpus()
    #for d in data:
    #    corpus.add_doc(d)
    #corpus.clean(stopwords=True,
    #            lower=True,
    #            clean_vowels=True,
    #            remove_numbers=True)
    #for d in corpus.docs:
    #    print(corpus.docs[d].trans)
    print(lambda_handler(data, 1))
