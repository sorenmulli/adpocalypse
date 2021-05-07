<template>
  <div class="home">
    <meta name="viewport" content="width=device-width, initial-scale=1">
     <div :style="{'backgroundImage':'../assets/back.jpg'}">
  </div>
    <h1>{{ msg }}</h1>
    <p>
        We charted interactions between characters in the world of <em>A Song of Ice and Fire</em> - both in the original books and in reader discussions.
    </p>
    <div class="bg" align="center" width=100% position="float">
      <a :href="require('../assets/back.jpg')" target="_blank">
            <img src="../assets/back.jpg" height=440 width=102%>
        </a>
      </div>
    <h3>What are we looking for?</h3>
    <div align="left">
      <p>
        <b>Worldbuilding</b>, the process of constructing imaginary universes, has intrigued audiences for as long as humanity has been telling stories. The detailed, gritty fantasy world of <em>A Song of Ice and Fire</em> (the book series on which Game of Thrones is based) is one of the most popular examples of this in the recent years.
      </p>
      <p>
          As worldbuilding, in our estimation, plays a growing role in popular literature and media, it is of interest to study how the readers relate to it - a relationship which American author John Harrison characterizes as negative, noting <q>Worldbuilding numbs the reader’s ability to fulfil their part of the bargain ...</q>, even suggesting that it might make us receptive to advertising and political rhetoric.
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
      </div>
    <h3>Two Graphs of Thrones</h3>
    <div align="left">
      <p>
        Now, we have the main ingredients ready: Two different text data sets filled to the brim with fictional characters.
        So, let's bake them into a nice stew by <b>building a social graph</b> for each of the two worlds of text!
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
        Hey! There is definitely a difference between these two social worlds.
    </p>
    <p>
        Certain characters such as Jon Snow and Tyrion Lannister are much more prominent in the Reddit texts, while the characters that are more important early on in the story such as Ned Stark, Robb Stark and Robert Baratheon have faded more from the discussions.
    </p>
    <p>
        There are also some links that are much clearer in the Reddit data: Here, we see a triangle of Daenarys, Tyrion and Jon Snow not seen in the book graph.
        These are three characters that are spatially far away from eachother in most of the story, but might be much more adjacent in space of Reddit discussions dealing with possible endings, wild theories and favorite characters.
    </p>
    <p>
       While interesting, the plots are pretty messy (even though we had to hide many weak links and lonely characters), so let us go beyond this qualitative zoom in on local graph differences and look for a way to <em>measure</em> what the difference is.
    </p>
    </div>
    <h3>What is going on in the two social worlds?</h3>
    <div align="left">
    <p>
        The easiest numbers to look at are the strengths of the links.
        The average weight of links - how often the characters occur in same chapter of post - is, in the books,  7% and is in average varies about 8% away from this typical value.
        For the reddit graph, these values are very different: 0.7% is the average strength and it varies typically 0.8%.
    </p>
    <p>
        This means that weights are in general <b>much</b> smaller in the discussion data:
        The readers talk about a large number of different character pairs -- it not just <em>all</em> the attractive pair Jon and Dany (those two fiery fighters <em>do</em> outperform the mean quite a bit by occurring in 8% of all discussions)
    </p>
    <p>
        When we plot the proportions for the entire list of characters (Fig. 3), we realize why the means are so different:
        In the actual story, there are some characters that meet quite rarely, many sometimes see each or discuss other and some are together in most chapters, but the (green) line between these is mostly uniform.
        In the discussions, however, most character pairs very rarely are mentioned together apart from a small number of much more popular outliers such as Jon and Dany, or Jon and Tyrion, or Jon and Bran, or Jon and ... - you get the picture!
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

    <h3>It's good to have cliques in a dragon world </h3>
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
        When we compare these partitions with the factions (families, political groups) in the fantasy world, it is seen that the book graph has highest correspondence, showing that the readers consider more than just geography and family when discussing the story.
        This faction grouping can be seen in the colours in the partitions and charted in the tables below.
    </p>
    <div align="center">
     <table>
     <caption>Tab. 1 - Communities found from the book chapter graph</caption>
        <tr>
            <th>Book Community</th>
            <th>Baratheon</th>
            <th>Tyrell</th>
            <th>Stark</th>
            <th>Lannister</th>
            <th>Other</th>
            <th>Night's Watch</th>
            <th>Targaryen</th>
            <th>Greyjoy</th>
        </tr>
        <tr>
            <td>Com. 1</td>
            <td>2</td>
            <td>1</td>
            <td>2</td>
            <td>9</td>
            <td>1</td>
            <td>0</td>
            <td>1</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Com. 2</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>4</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Com. 3</td>
            <td>2</td>
            <td>0</td>
            <td>5</td>
            <td>0</td>
            <td>3</td>
            <td>3</td>
            <td>0</td>
            <td>1</td>
        </tr>
     </table>
     <table>
        <caption>Tab. 2 - Communities found from the Reddit post graph</caption>
        <tr>
            <th>Reddit Community</th>
            <th>Baratheon</th>
            <th>Tyrell</th>
            <th>Stark</th>
            <th>Lannister</th>
            <th>Other</th>
            <th>Night's Watch</th>
            <th>Targaryen</th>
            <th>Greyjoy</th>
        </tr>
        <tr>
            <td>Com. 1</td>
            <td>3</td>
            <td>0</td>
            <td>3</td>
            <td>0</td>
            <td>1</td>
            <td>3</td>
            <td>4</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Com. 2</td>
            <td>0</td>
            <td>0</td>
            <td>4</td>
            <td>2</td>
            <td>3</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
        </tr>
        <tr>
            <td>Com. 3</td>
            <td>1</td>
            <td>1</td>
            <td>0</td>
            <td>7</td>
            <td>0</td>
            <td>0</td>
            <td>1</td>
            <td>0</td>
        </tr>
      </table>
    </div>
    <p>
        Overall, these partitioning differences reveal natural domain differences.
        The discussion realm is not bound by geographic limits and obvious character interactions; the fan discussions transcend the merely descriptive and find parallels in different storylines, possibly providing a counter argument to the Ben Harrison's point about the reader laziness in wordbuilding literature.
    </p>
    </div>
    <h3>But what about all that text?</h3>
    <div align="left">
        <p>
            The above gave us some insight into differences between the social world created by the author and the one in the reader discussions.
            But, to find more differences than social links, we need to <b>consider more of the text</b> than just whether two characters appear together.
        </p>
          <div align="center" class=bg1 width=100% position="float">
        <a :href="require('../assets/bogen.png')" target="_blank">
              <img src="../assets/bogen.png" height=420 width=102%>
          </a>
        </div>
        <p>
            In order to determine if the characters are defined by the same words in the book compared to the subreddit, we start counting up the words that appear together with the names of the characters.

            Let us release our inner worldbuilding nerds on these character word clouds.
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
        <div align="center">
             <h3>Dispersion plots </h3>
             <p>
                In order to compare the language of the game of thrones readers to the language of the book series - we've constructed several dispersion plots.
                We have chosen to look at the most frequent terms from the subreddit to see if these are words used in the book and furthermore if these words
                are used in the context of the specific character.
            </p>
        </div>
      <div align="center">
      <figure>
        <a :href="require('../assets/dispersion_dany_reddit.png')" target="_blank">
            <img src="../assets/dispersion_dany_reddit.png" width=600>
        </a>
      <figcaption>
        Fig. 5 -
        A dispersion plot of the most frequent terms on the subreddit in describing Daenarys.
        (Click image for larger)
      </figcaption>
      </figure>
    </div>
    <p>
      Some of the most defining words for Daenarys in the minds of the redditors are aegon, dragon, whtie, blood and iron. Interestingly, the language used
      by the redditors correspond to the language used in the books. This may suggest that the redditors have adopted the language of the book.
      We furthermore see that words such as aegon and dragon are mentioned with almost the same frequency as Daenarys in the book series.
    </p>
        <div align="center">
      <figure>
        <a :href="require('../assets/dispersion_tywin_reddit.png')" target="_blank">
            <img src="../assets/dispersion_tywin_reddit.png" width=600>
        </a>
      <figcaption>
        Fig. 6 -
        A dispersion plot of the most frequent terms on the subreddit in describing Tywin.
        (Click to enlarge)
      </figcaption>
      </figure>
    </div>
    <p>
      Father and Lord are two defining terms for Tywin from the redditors. However, these are very frequently used words
      in the book which again might suggest that the redditors has adopted the language. Prince does seem to have the same frequency
      as Tywin himself which could mean that this is a defining word for the character in the book as well as in the mind of the subreddit.
    </p>
      <div align="center">
      <figure>
        <a :href="require('../assets/dispersion_jon_reddit.png')" target="_blank">
            <img src="../assets/dispersion_jon_reddit.png" width=600>
        </a>
      <figcaption>
        Fig. 7 -
        A dispersion plot of the most frequent terms on the subreddit in describing Jon.
        (Click to view big)
      </figcaption>
      </figure>
    </div>
    <p>
      Many of the words used by redditors to define Jon Snow are frequently used in the book. This, would to some extend confirm
      the hyphothesis that the redditors have adopted the language used in the books series a song of ice and fire.
    </p>
      <figure>
        <a :href="require('../assets/pca_book.png')" target="_blank">
            <img src="../assets/pca_book.png" width=900>
        </a>
      <figcaption>
        Fig. X -
        (Click to view big)
      </figcaption>
      </figure>
      <figure>
        <a :href="require('../assets/pca_reddit.png')" target="_blank">
            <img src="../assets/pca_reddit.png" width=900>
        </a>
      <figcaption>
        Fig. Y -
        (Click to view big)
      </figcaption>
      </figure>
    <h3>Tell me yours and I'll tell you mine</h3>
    <div align="left">
    <p>
        Now that we have seen which words describe characters and how characters can be put into different communities, we want to investigate
        an even more important question: Who does Reddit have the hots for? Who does Reddit have it out for? Are Redditors - one of the most
        opinionated platforms on the planet - have characters they seem to be neutral towards? It is time to find out with the illustration below,
        showing redditor sentiment, their attitude, for five interesting characters.
    </p>
    </div>
    <div align="center">
        <img class="crop-height" src="../assets/sentiment_analysis.png" width=550>
    </div>
    <div align="left">
    <p>
        Immediately, we notice that the text of some of the characters reach outside of the plot borders. A shame, but we have much more important
        results to discuss! Firstly, we see that we finally have an answer to whether Joffrey or Ramsey is the most hated; Reddit answers a resounding
        Ramsey. It definitely makes sense that both are scraping the bottom of the hate barrel based on their ruthless and vile behaviour. <b> MORE ABOUT
        THE CHARACTERS</b>
    </p>
    <p>
        Another quick point is that the VADER sentiment analysis actually gets widely different answers than the dictionary-based sentiment analysis. This
        and much more can be examined in detail in our notebook tailor-made for this project. It contains all the code used to make
        the plots and get the results you have been enjoying throughout this website. Come have a look, we look forward to being shamed for using try except
        statements instead of handling errors like adults.
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
<style lang="scss">
 table {
  width: 60%;
 }
 table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
 th {
  text-align: left;
}
tr:nth-child(even) {
  background-color: #eee;
}
tr:nth-child(odd) {
  background-color: #fff;
}
th {
  color: white;
  background-color: grey;
}
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
.bg {
  /* The image used */
  background-image: url("../assets/back.jpg");

  /* Full height */
  height: 100%;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
.bg1 {
  /* The image used */
  background-image: url("../assets/bogen.png");

  /* Full height */
  height: 100%;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: 790px;
}
</style>
