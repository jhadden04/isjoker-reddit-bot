from urllib.parse import quote_plus
from datetime import datetime
import praw

IGNORE = ["subreddit", "redditors", "b"]
SEARCH = ["good", "yes", "reddit"]
CHANNELS = "all"
REPLY_TEMPLATE = "[I found something for you!]({})"


def main():
    reddit = praw.Reddit(client_id='O-gpEre-AApeVw',
                         client_secret='OFL5X-qnNiHx4kIefPJEpLemKCc',
                         user_agent='a reddit instance',
                         username='loverofgirl32',
                         password='pulapula', )

    subreddit = reddit.subreddit(CHANNELS)
    for submission in subreddit.stream.submissions():
        process_submission(submission)


def process_submission(submission):
    # check to see if it is WTB or META, ignore these
    normalized_title = submission.title.lower()
    normalized_desc = submission.selftext.lower()

    # Start of the new search feature, fingers crossed.
    # for any_line in normalized_desc:
    for search in SEARCH:
        if search in normalized_title:
        # if any(word in any_line for word in SEARCH):
            present_info(submission)

    # This is the start of the original search, not working well. missing a lot
    for ignore_phrase in IGNORE:
        if ignore_phrase in normalized_title:
            # return changed to break
            break
        # only remaining SHOULD be for SALE or TRADE

    '''for search_phrase in SEARCH:
        if search_phrase in normalized_desc:
            present_info(submission)
            # break'''


##    #original
##    for question_phrase in SEARCH:
##        if question_phrase in normalized_desc:
##            present_info(submission)
##            #break


def present_info(submission):
    # present the info nicely, probably make a function for this
    timestamp = submission.created_utc
    dt_object = datetime.fromtimestamp(timestamp)
    url_link = submission.url
    print(submission.subreddit)
    print('Posted by u/{} * {}'.format(submission.author,
                                       dt_object))
    print(submission.title, '\n')
    print(REPLY_TEMPLATE.format(url_link))
    print('===========')


if __name__ == "__main__":
    main()

##1. check to see if the post is selling
##2. check title to see if it contains keyword
##3. if it does, do stuff, otherwise
##4. check description to be sure
##5. same as 3
##6. ignore
