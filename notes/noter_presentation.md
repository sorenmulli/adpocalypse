## Notes for the presentation, YT!

### "funny" introduction

1. Welcome to the world of game of thrones; where the characters are plentiful and complicated, and the shock value is more for show than for actual character development. If season 8 has taught us anything, it is that for the show to be any good, we have to write it ourselves. To do so, it would help to have a good understanding of how the most important characters in the books interact with and relate to each other. Meanwhile, it is also important to satisfy the neckbeard stans on reddit. In other words, we want to find the relations between characters in the hivemind of reddit and in the actual books.

### Size and origins of social graphs

2. This will be possible using two social graphs; one constructed using the text from the ebooks and one constructed using posts on the r/asoiaf subreddit. For the ebook social graph, every character is a node and a link is created if two characters are mentioned in the same chapter. This leads to a network with 34 nodes and 505 links and a dataframe of $\textbf{ROWS}$ rows and $\textbf{VARIABLES}$ variables. For the reddit data, we extracted every submission title and text between $\textbf{DATE1}$ and $\textbf{DATE2}$. We removed all submissions without text and where no characters are mentioned. Afterwards, we connected the character nodes with links if they are mentioned in the same submission. This left us with a dataframe with $\textbf{ROWS}$ rows where the kept variables are selftext and title. Building a network of this dataframe gives a network with 34 nodes and $\textbf{LINKS}$ links and The number of nodes shows that every character is mentioned in both reddit and the books. Meanwhile, the final pandas dataframe have $\textbf{ROWS}$ rows and $\textbf{VARIABLES}$ variables in total.

### What do we do from here?
  
3. With these two social graphs, we see a substantial difference between how Reddit views the character relations vs how the characters actually relate. This means that for project B, 
