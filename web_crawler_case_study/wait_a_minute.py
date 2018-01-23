# Work out the final step in the while loop - how to make Python wait for two seconds. You might need to do some
# research to find a relevant Python package and/or command to use. Add an import statement to the top part if
# needed, and then a line of code at the bottom of the indented block.

#TODO: import something?

import time

def web_crawl():
    while continue_crawl(article_chain, target_url):
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        article_chain.append(first_link)
        # delay for about two seconds
        # TODO: YOUR CODE HERE!
        time.sleep(2)