# The continue_crawl Function The first helper function we need to write is continue_crawl which will be used in our
# while loop like this:
#
# while continue_crawl(search_history, target_url):
# For example, we might call the function with these values:
#
# continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'], 'https://en.wikipedia.org/wiki/Philosophy')
# search_history is a list of strings which are the urls of Wikipedia articles. The last item in the list most
# recently found url. target_url is a string, the url of the article that the search should stop at if it is found.
# continue_crawlshould return True or False following these rules:
#
# if the most recent article in the search_history is the target article the search should stop and the function
# should return False If the list is more than 25 urls long, the function should return False If the list has a cycle
#  in it, the function should return False otherwise the search should continue and the function should return True.
# For this quiz, implement continue_crawl. For each of the situations where the search stops, print a message that
# briefly explains why. Remember to test your code!

multiple_url = ['https://en.wikipedia.org/wiki/Floating_point'] * 25

def continue_crawl(search_history, target_url, max_steps=25):
    """
    :param max_steps: number of search_history allowed
    :param search_history: search_history is a list of strings which are the urls of Wikipedia articles. The last
    item in the list most recently found url.
    :param target_url: target_url is a string, the url of the article that
    the search should stop at if it is found.
    :return: a boolean (True or False):
    If the most recent article in the search_history is the target article the search should stop and the function
    should return False
    If the list is more than 25 urls long, the function should return False
    If the list has a cycle in it, the function should return False
    otherwise the search should continue and the function should return True.
    """
    count_links = 0
    if search_history[-1] == target_url:
        print("We've found our target URL!")
        return False
    if len(search_history) > max_steps:
        print('Halt! Max steps reached!')
        return False
    if search_history[-1] in search_history[:-1]:
        print('Cease! Cycle detected!')
        return False
    return True


print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],
                     'https://en.wikipedia.org/wiki/Philosophy'))

print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point', 'https://en.wikipedia.org/wiki/Floating_point'],
                     'https://en.wikipedia.org/wiki/Philosophy'))

print(continue_crawl(['https://en.wikipedia.org/wiki/Philosophy'],
                     'https://en.wikipedia.org/wiki/Philosophy'))

print(continue_crawl(multiple_url, 'https://en.wikipedia.org/wiki/Philosophy'))
