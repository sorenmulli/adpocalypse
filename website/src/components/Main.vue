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
          As worldbuilding, in our estimation, plays a growing part in popular literature and media, it is of interest to study how the readers relate to it - a relationship which American author John Harrison characterizes as negative, noting <q>Worldbuilding numbs the reader’s ability to fulfil their part of the bargain ...</q>, even suggesting that it might make us receptive to advertising and political rhetoric.
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
        The readers talk about a large number of different character pairs -- it not just <em>all</em> the attractive pair Jon and Dany (those two fiery fighters <em>do</em> outperform the mean quite a bit by occurring in 8% of all discussions)
    </p>
    <p>
        When we plot the proportions for the entire list of characters (Fig. 3), we realize why the means are so different:
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
      This is not the only finger print of such social graphs:
      We also measure how often a character's friends are also friends themselves.
      Compared to the mean connection strengths, these <em>clusterings</em> of the two graphs are much closer together, implying that there are also closely-knitted groupings of characters in the Reddit graph.
    </p>
    <p>
      When considering how strong the links between any two characters are, by considering longest paths, we see the same not quite clear picture:
      It is easier to find characters that often occur between
    </p>
    <p>
    </p>
    </div>

    <div align="left">
    <p>
        To get a clearer picture of how the two graphs really differ, <b>the communities</b> of the two graphs are found by answering the question:
        <q> Which hubs of characters appear together so often that it would not happen at random? </q>
        The answer to this algorithmic question is given in the figure below.
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
       For the book graph, a fan of the series will recognize the defining factor of the three found graph communities:
       Geography!

       All the characters in book community 1 are found around the capital region of the universe, the ones in community 2 are found in the far east and the third community corresponds somewhat clearly to the icy North.
    </p>
    <p>
        The Reddit graph groupings do have some similarities to the above: Community 3 corresponds quite well to the book community 1, although the reader community can be better described using the abstract concept of the royal court rather than the geographic region.

        The first community contains many of the characters that are main actors in the central storyline: Jon Snow, Dany, Ned Stark, Bran Stark, and as such would often be discussed together.
        Reddit community 2 seems centred on the two Stark sisters, Arya and Sansa, and their mother.
        This community includes many people that at different points in the stories protect both of the daughters, thus revealing how connected the stories of these two daughters are, even though they are no geographically close all through the story.
    </p>
    <p>
        Overall, these partitioning differences reveal natural domain differences.
        The discussion realm is not bound by geographic limits and obvious character interactions; the fan discussions transcend the merely descriptive and find parallels in different storylines, possibly providing a counter argument to the Ben Harrison's point about the reader laziness in wordbuilding literature.
    </p>
    </div>

    <div align="left">
        <p>
            The above gave us some insight into differences between the social world created by the author and the one in the reader discussions.
            But, to understand more differences than the social ones, we need to <b>consider more of the text</b> than just whether two characters appear together.
        </p>
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
        <div class="row" align="center">
            <div class="column" align="center">
                <img class="crop-height" src="../assets/dany_TF_wordcloud.png" width=550>
            </div>
            <div class="column" align="center">
                <img class="crop-height" src="../assets/dany_TF_book.png" width=550>
            </div>
        </div>
        <p>
            On the left hand is the word cloud constructed from the reddit data and on the right hand side is the worldcloud from the book.
            We do see some overlap in these word clouds; blood, dragon, lord, old, daenerys, tyrion. This might suggest that there are some overlap between
            the fantasy universe from the book and the universe in the mind of the redditors - at least on how Daenerys is percieved. However,
            we also see differences between the most frequent terms for Daenerys; season, love, aegon. Aegon is Daenerys brother and is potrayed in
            the books as he will play a big role in the story. This has resulteted in a lot of debate about this character on the subreddit, but
            his storyline in the book never progressed. In conclusion, the words that describe Daenarys in the books compared to the subreddit are
            surprisingly similar which suggest that the fantasy universe intended by George R. R. Martin has latched on to its readers. Lets see if this
            holds true for all characters.
        </p>
          <div class="row" align="center">
            <div class="column" align="center">
                <img class="crop-height" src="../assets/tywin_TF_wordcloud.png" width=550>
            </div>
            <div class="column" align="center">
                <img class="crop-height" src="../assets/tywin_TF_book.png" width=550>
            </div>
        </div>
        <p>
        On the left: Reddit data. On the right: Book data. Again, we see a lot of overlap between each of these word clouds. Most notably;
        Tyrion, lord, father, Cersei, Jaime. The differences are; Aerys, love, Rhaegar, black. Again, we see a great overlap, but some even
        more interesting differences. Aerys (also known as the mad king) is mentioned a lot on the subreddit, but has less focus in the books.
        Arya and Tywin meet in tv-show but never in the book. This, might be why she is in the reddit wordcloud but not in the book cloud.
        We still see a lot of overlap but some more noticeable differences. Will this hold true for the next character?
        </p>
           <div class="row" align="center">
            <div class="column" align="center">
                <img class="crop-height" src="../assets/jon_TF_wordcloud.png" width=550>
            </div>
            <div class="column" align="center">
                <img class="crop-height" src="../assets/jon_TF_book.png" width=550>
            </div>
        </div>
        <p>
        On the left: Reddit data. On the right: Book data. Jon
        </p>
        </div >
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
/* Three image containers (use 25% for four, and 50% for two, etc) */
.column {
  float: left;
  width: 49%;
  padding: 0px;
}

/* Clear floats after image containers */
.row::after {
  content: "";
  clear: both;
  display: table;
}
.crop-height {
    /* max-width: 1200px; /* img src width (if known) */
    max-height: 600px;
    overflow: hidden; }
</style>
