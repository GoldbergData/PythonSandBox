# Time to write your own loop with a break statement. Your task is to create a string, news_ticker that is exactly
# 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a
# space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is
# exactly 140 characters long.

# Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding
# print statements to your code to help you resolve bugs.

def create_news_ticker(input_list):
    news_ticker = []
    char_len = 0
    last_ticker = []
    loops = 0
    limit = 0
    for headline in headlines:
        if char_len + len(headline) > 140:
            limit = len(news_ticker)
            loops = 140 - limit - char_len
            last_ticker = headline
            last_ticker_merged = ''
            i = 0
            while loops > 0:
                last_ticker_merged += last_ticker[i]
                loops -= 1
                i += 1
            news_ticker.append(last_ticker_merged)
            return(' '.join(news_ticker))
        news_ticker.append(headline)
        char_len += len(headline)

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = create_news_ticker(headlines)
print(news_ticker)
print(print("final: news_ticker length: {}".format(len(news_ticker))))
# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs