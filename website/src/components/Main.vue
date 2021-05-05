<template>
  <div class="home">
    <h1>{{ msg }}</h1>
    <p>
        We charted interactions between characters in the world of <em>A Song of Ice and Fire</em> - both in the original books and in reader discussions.
    </p>

    <h3>What are we looking for?</h3>
    <div align="left">
      <p>
        <b>Worldbuilding</b>, the process of constructing imaginary universes, has intrigued audiences for as long as humanity has been telling stories. The detailed, gritty fantasy world of <em>A Song of Ice and Fire</em> (the book series on which Game of Thrones is based) is one of the most popular examples of this in the recent years.
      </p>
      <p>
          As worldbuilding, in our estimation, plays a growing part in popular literature and media, it is of interest to study its effect the readers - an effect which American author John Harrison characterizes as negative, noting <q>Worldbuilding numbs the reader’s ability to fulfil their part of the bargain ...</q>, even suggesting that it might make us receptive to advertising and political rhetoric.
      (John Harrison: "Very Afraid", 2007, Online, Fetched 05/05-21 <a href="http://web.archive.org/web/20080410181840/http://uzwi.wordpress.com/2007/01/27/very-afraid" target="_blank">here</a>)
      </p>
      <p>
          A newer dynamic added to the relationship between the worldbuilder (author) and the world explorers (readers) is the emergence of large-scale always-on discussion fora where no detail in the fantasy world is left undiscussed.
      </p>
      <p>
          We want to understand this dynamic better by taking <em>A Song of Ice and Fire</em> as a case study.
      </p>
    </div>

    <h3>Data!</h3>
    <div align="left">
      <p>
        <ol>
            <li>
              <img src="https://media.vanityfair.com/photos/53235792932cac31720001be/master/w_2560%2Cc_limit/george-rr-martin.jpg" width=80>
              The text for all five books in <em>A Song of Ice and Fire</em>: 7M words divided into 358 chapters.
            </li>
            <li>
              <img src="https://i.imgur.com/sdO8tAw.png" width=80>
              Scrape from 2015-2018 of 70K reddit posts from the book discussion subreddit (forum) <a href="https://www.reddit.com/r/asoiaf/" target="_blank"> /r/asoiaf </a> totalling 15M words.
            </li>
        </ol>
      </p>
      <p>
        Now, let's <b>build a graph</b> for each of the two worlds of text!
      </p>
    </div>
    <div align="center">
      <figure>
        <a :href="require('../assets/book_graph.png')" target="_blank">
            <img src="../assets/book_graph.png" width=900>
        </a>
        <figcaption>
        Fig. 1 - The graph of character relationships in the books:
        We strengthen the link between two characters every time they appear in the same chapter. (Click image for larger) </figcaption>
      </figure>
      <br>
      <figure>
        <a :href="require('../assets/reddit_graph.png')" target="_blank">
            <img src="../assets/reddit_graph.png" width=900>
        </a>
        <figcaption>
        Fig. 2 - The graph of character relationships in the reddit data:
        Here, we make the links stronger for each reddit discussion post that mention both characters (Click image for larger)
        </figcaption>
      </figure>
    </div>
    <div align="left">
    <p>
        Hey! There is definitely a difference between these two graphs.
    </p>
    <p>
        Certain characters such as Jon Snow and Tyrion Lannister are much more prominent in the Reddit texts, while the characters that are more important early on in the story such as Ned Stark, Robb Stark and Robert Baratheon have faded more from the discussions.
    </p>
    <p>
        There are also some links that are much clearer in the Reddit data: Here, we see a triangle of Daenarys, Tyrion and Jon Snow not seen in the book graph.
        These are three characters that are spatially far away from eachother in most of the story, but might be much more adjacent in space of Reddit discussions dealing with possible endings, wild theories and favorite characters.
    </p>
    <br>
    <p>
        Instead of only looking at what the graphs <b>look</b> like, we also want to look at some numbers. The average weight of links -how strong the connection is between characters- for charcters in the books is 7.49 and the standard deviation is 7.87. For the reddit graph, these values are instead 0.67 and 0.79. This means that weights are in general <b>much</b> smaller in the reddit data, which makes sense since we divide by the total number of possible occurrences. Unsurprisingly, this sentiment is shared by the plot below!
    </p>
    </div>
    <div align="center">
          <figure>
        <a :href="require('../assets/comention_dist.png')" target="_blank">
            <img src="../assets/comention_dist.png" width=900>
        </a>
        <figcaption>Fig. 3 - The graph of how the strength of links is distributed: we see that most of the links are very weak. (Click image for larger) </figcaption>
    </figure>
    </div>
    <div align="left">
    <p>
        But wait, there's more! We have two more numbers that can tell you a lot about any graph.
    </p>
    <p>
        The first one is the average shortest path. The average shortest path expresses how far you can expect to travel between any two locations in a network. As such, a larger average shortest path means that you will need to pack hiking shoes instead of crocs. The average shortest path of the book graph is 0.0122 and it is 0.0011 for the reddit graph. This shows that it is generally easier to get around in the reddit graph.
    </p>
    <p>
        The other interesting number is the average clustering. The average clustering of a network says something about how clumped together nodes are in general in a network. As such, a larger average clustering of buildings in a city means that you are more likely to be in Osaka, Japan than Roskilde, Denmark. The average clustering is 0.1600 for the book graph and 0.0811 for the reddit graph. This means that the nodes of the book graph are generally more clumped together.
    </p>
    <p>
        Besides all of this, while interesting, we want to go beyond this qualitative zoom in on local graph differences and look for a way to <em>measure</em> what the difference is.
    </p>
    </div>

    <h3>What is revealed?</h3>
    <div align="left">
    <p>
        <b>The communties</b> of the two graphs are found by answering the question:
        <q> Which hubs of characters often appear together? </q>

        <!--Udkommenteret: Tænker, det skal ind i notesbogen i stedet

        We used community detection on the 34 most notable characters of Game of Thrones on both the books and on reddit. This will allow us to see if redditors prioritize the character relations in the same way as the books do and if characters are usually mentioned in relation to their factions, like one might expect. The result of this analysis can be seen in the four pictures below. The two first pictures are the communities found in the book and on reddit respectively. The two next
        pictures are how one might expect the communities to look if characters were only mentioned along with other characters from the same faction.-->
    </p>
    <div align="center">
        <img src="../assets/communities_book.png">
        <br>
        <img src="../assets/communities_reddit.png">
        <img src="../assets/communities_true_reddit.png">
    </div>
    <p>
        Now these plots are interesting! The characters that have been linked are the ones that are most often mentioned together. Every character is mentioned to some extent, so these illustrations only show the MOST mentioned characters. Now what do we see from these illustrations?
        Well, in the graph of the book mentions, we see that the Starks and Lannisters are mentioned together like expected and as can be seen in the true graph.
    </p>
    </div>

   </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Home',
  props: {
    msg: String
  }
})
</script>
