#!/usr/bin/env python
import praw
import numpy

def get_value( name, google_rank ):

    user_agent = "MEMEZ by MEMEZ"
    amount = 1000
    counter = 0
    final_rank = google_rank * 10
    results = []
    r = praw.Reddit(user_agent=user_agent)
    subreddit_names = "blobo+memes+adviceanimals+harambe+pepe+pepethefrog+freshmemes+dank_meme+dankmemes+datboi"

    name = name.lower()
    memes = r.get_subreddit(subreddit_names).get_top_from_day(limit = amount + 1)

    for meme in memes:
        if counter == 5:
            break
        if name in meme.title.lower():
            results.append(meme.score)
            counter += 1
    if results:
        final_rank += numpy.median(numpy.array(results))
        if final_rank < 0:
            final_rank = 0
    return final_rank
