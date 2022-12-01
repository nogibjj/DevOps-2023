"""
Build a library of wikipedia tools.
"""
import wikipedia
import yake

# create a function to return the summary of a wikipedia page
def get_wiki_summary(search_term):
    """Return the summary of a wikipedia page."""
    # get the summary of the wikipedia page
    summary = wikipedia.summary(search_term)
    # return the summary
    return summary


# create a function to search for the best match for a wikipedia page
def get_wiki_page_content(search_term):
    """Return the best match for a wikipedia page."""
    # get the best match for the wikipedia page
    page = wikipedia.page(search_term)
    # return the page
    return page


# create a function to return the keywords of a wikipedia page
def get_wiki_keywords(search_term):
    """Return the keywords of a wikipedia page."""
    # get the keywords of the wikipedia page
    page = wikipedia.page(search_term)
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(page.content)
    # return the keywords
    return keywords
