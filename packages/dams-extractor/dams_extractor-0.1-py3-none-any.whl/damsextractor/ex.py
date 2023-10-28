try:
    import requests
except ImportError:
    raise ImportError("The package 'requests' is not installed.")

try:
    from boilerpy3 import extractors, exceptions as bpe
except ImportError:
    raise ImportError("The package 'boilerpy3' is not installed.")

try:
    from nltk.tokenize import sent_tokenize
except ImportError:
    raise ImportError("The package 'nltk' is not installed. Once installed, install the 'punkt' tokenizer")

EXCTRACTOR = extractors.NumWordsRulesExtractor()
HEADERS = {
    'User-Agent': 'Mozilla/5.0'
}

#Input: 
# 'url': A valid privacy policy website url to extract from
# 'tokenized': Specifies if a string is returned, or a sentence
#              tokenized list using the 'punkt' dataset from nltk
#Output:
# str, list, or None if an error exists
def extractText(url, tokenized=False):

    #Attempt to retrieve the webpage
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.InvalidSchema:
        return None
    
    #Attempt to extract policy contents
    try:
        content = EXCTRACTOR.get_content(response.text)
        content = content.replace('\n', ' ')
    except bpe.HTMLExtractionError:
        return None

    #Tokenize the extracted text if specified
    if tokenized:
        content = sent_tokenize(content)

    return content