# Write a line of code that will add the first_link to the end of the list article_chain. This line should come after
# the comment, "add the first link to article chain".

def web_crawl():
    while continue_crawl(article_chain, target_url):
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        article_chain.append(first_link)
        # delay for about two seconds