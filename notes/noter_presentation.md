## Notes for the presentation, YT!

### "funny" introduction

1. Welcome to the world of game of thrones; where the characters are plentiful and complicated, and the shock value is more for show than for actual character development. If season 8 has taught us anything, it is that for the show to be any good, we have to write it ourselves. 
<br>
To do so, it would help to have a good understanding of how the most important characters in the books interact with and relate to each other. We do this by creating one social graph from the books and one from reddit data.
<br>
Apart from satisfying the redditor neckbeard nerds, this analysis can explore whether the social structure of fictive worlds is the same in the minds of the fans as it is in the original work.

### Size and origins of social graphs

2. This will be possible using two social graphs; one constructed using the ebook text from the five books and one constructed using posts on the r/asoiaf subreddit downloaded using PushShift. <br><br>
The 5 books consist of 358 chapters which takes up 10 MB space and totals around 2M words. <br><br>
From reddit, we have collected 100MB data from 70k submissions posted before the release of season 8 which give us a corpus of 15M words. <br><br>
For both graphs, the 34 nodes correspond to each characters.  <br><br>
In the book graph, we link them if two characters are mentioned in the same chapter giving us 472 links <br><br> And in the reddit graph, they are linked if characters are mentioned in the same post which ends up up in 560 links. <br><br>
The social graph from the book has an average degree of 28, while it is 33 for the Reddit graph.
Therefore there are no dramtic differences between the degree distribution of the two graphs. <br><br>


### Where do we go from here?
  
Now, we really want to understand the differences in the character relations.

The data gives us many options here:

First of all, we weight the links by number of co-mentions and we want to understand the differences in the weight distributions between the two domains.

The next step is to find communities in these social graphs.
Are they the same in both graphs - and does community detection reveal the factions we know from the world?

The opportunities for analysis using natural language processing on both the book texts and reddit selftexts are plentiful.

We want to use this to explain the causes of graph differences and visualize the character personalitites using word clouds and frequency diagrams.

Ultimately, we hope this can give us an insight into how fandoms treat fantasy universes -- while also having some fun with this bloody world of intrigues and dragons.
