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
    <p>
       While interesting, we want to go beyond this qualitative zoom in on local graph differences and look for a way to <em>measure</em> what the difference is.
    </p>
    </div>
    <h3>What is revealed?</h3>
    <div align="left">
    <p>
        The easiest numbers we can look at are the strengths of the links.
        The average weight of links - how often the characters occur in same chapter of post - is, in the books, is 7% and varies about 8% away for this typical value.
        For the reddit graph, these values are very different: 0.7% is the average strength and it varies typically 0.8%.
    </p>
    <p>
        This means that weights are in general <b>much</b> smaller in the discussion data:
        The readers talk about a large number of different character pairs -- it not just <em>all</em> the attractive pair Jon and Dany (those two fiery fighters <em>do</em> outperform the mean quite a bit by occuring in 8% of all discussions)
    </p>
    <p>
        When we plotthe proportions for the entire list of characters (Fig. 3), we realize why the means are so different:
        In the actual story, there are some characters that meet quite rarely, many sometimes see each or discuss other and some are together in most chapters, but the (green) line between these is mostly uniform.
        In the discussions, however, most character pairs very rarely are discussed together with a small number of much more popular outliers such as Jon and Dany or Jon and Tyrion ... or Jon and Bran - you get the picture!
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
        <!---TODO: Kommet hertil i gennemretning-->
        The first one is the average shortest path.
        The average shortest path expresses how far you can expect to travel between any two locations in a network.
        As such, a larger average shortest path means that you will need to pack hiking shoes instead of crocs.
        The average shortest path of the book graph is a hundred times

        0.0122 and it is 0.0011 for the reddit graph.
    </p>
    <p>
        The other interesting number is the average clustering. The average clustering of a network says something about how clumped together nodes are in general in a network. As such, a larger average clustering of buildings in a city means that you are more likely to be in Osaka, Japan than Roskilde, Denmark. The average clustering is 0.1600 for the book graph and 0.0811 for the reddit graph. This means that the nodes of the book graph are generally more clumped together.
    </p>
    <p>
    </p>
    </div>

    <div align="left">
    <p>
        <b>The communties</b> of the two graphs are found by answering the question:
        <q> Which hubs of characters often appear together? </q>

        <!--Udkommenteret: Tænker, det skal ind i notesbogen i stedet

        We used community detection on the 34 most notable characters of Game of Thrones on both the books and on reddit. This will allow us to see if redditors prioritize the character relations in the same way as the books do and if characters are usually mentioned in relation to their factions, like one might expect. The result of this analysis can be seen in the four pictures below. The two first pictures are the communities found in the book and on reddit respectively. The two next
        pictures are how one might expect the communities to look if characters were only mentioned along with other characters from the same faction.-->
    </p>
    <div align="center">
      <figure>
        <a :href="require('../assets/communities.png')" target="_blank">
            <img src="../assets/communities.png" width=1200>
        </a>
      <figcaption>
        Fig. 4 -
        For each graph, three <em>communities</em> were found revealing that the groups of characters that often go together are quite different in the books and in the Reddit discussions.
        (Click image for larger)
      </figcaption>
      </figure>
    </div>
    <p>
        <!--Udkommenteret: Vi skal lige se, om dette stadig er relevant
        Now these plots are interesting! The characters that have been linked are the ones that are most often mentioned together. Every character is mentioned to some extent, so these illustrations only show the MOST mentioned characters. Now what do we see from these illustrations?
        Well, in the graph of the book mentions, we see that the Starks and Lannisters are mentioned together like expected and as can be seen in the true graph.
        -->
    </p>
    </div>

    <h2>How are the characters described in the book compared to the subreddit Asioaf? </h2>
    <div align="left">
        <p>
            In order to determine if the characters are defined by the same words in the book compared to the subreddit several approaches
            to this can be taken. In the following three different characters will be analyzed to show some of the differences from the subreddit
            and the books. For the rest of the characters worldclouds can be found in the notebook or in our game section. To understand the three characters
            more deeply, we will look into four things:<br><br> Term frequency (TF), term frequency - inverse document frequency
            (TF-IDF), word clouds as well as the lexical dispersion of words from reddit in the book series. <br>
            <br>
            <b>Term frequency</b> <br> Term-frequencies cannot capture whether the term in a deeper sense characterizes the specific character, that is; is
             the frequency high because the term is especially important to the character or because it is just commonly used?
             Such as the terms <em> lord </em> and <em> ser </em> from the books. When counting occurences this interesting difference is not revealed.<br>
             <br>
             <b>Term Frequency - Inverse Document Frequency</b>
             <br> So, what is the difference bettwen TF and TF-IDF? The inverse document frequency is mathematically defined as
             as a logarithmically scaled inverse fraction of documents containg the word, such that only the relative scaling is of importance.
             The TF-IDF words are much more descriptive, as they contain more unique information about characters such as jokes about the sentiment towards the
             character and special names of people related to the character. Thus, this will allow to find more descriptive words of of the characters from the
             point of redditors and the book series respectively. This descriptiveness comes from the specificity that gives extra weight to terms that occur
             rarely in the corpus and thus, understood informally, carries more information about this particular document.<br>
             <br>
             <b>Word Cloud</b>
             <br> Word clouds are visual representations of text. In the case of this project we've used Word Clouds to illustrate
              the most frequest words specified to each character in Game of Thrones both from reddit and from the books.
              The following three word clouds represents Daenerys Targaryen, Tywin Lannister and Jon Snow.
        </p>
        <div class="crop" align="right" id=div_1>
            <img src="../assets/dany_TF_wordcloud.png">
          <!--  <img src="../assets/dany_TF_wordcloud.png">
            <img src="../assets/tywin_TF_wordcloud.png">
            <img src="../assets/tywin_TF_wordcloud.png">
            <img src="../assets/jon_TF_wordcloud.png">
            <img src="../assets/jon_TF_wordcloud.png">-->
        </div>
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
<style lang="scss">
 .crop {
        width: 660px;
        height: 250px;
        overflow: hidden;
    }

    .crop img {
        width: 380px;
        height: 300px;
        margin: -75px 0 0 -100px;
    }
</style>
