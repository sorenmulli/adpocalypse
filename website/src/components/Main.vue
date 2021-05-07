<template>
  <div class="home">
    <meta name="viewport" content="width=device-width, initial-scale=1">
     <div :style="{'backgroundImage':'../assets/back.jpg'}">
  </div>
    <h1>{{ msg }}</h1>
      <svg width="100%" viewBox="4 90 1250 77" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1">
      <path id="path">
        <animate attributeName="d" from="m410,110 h0" to="m410,110 h1100" dur="6.8s" begin="0s" repeatCount="indefinite" />
      </path>
      <text font-size="28" font-family="Montserrat">
        <textPath xlink:href="#path">A Song of Ice and Network Science!
        </textPath>
      </text>
    </svg>
       <div class="bg" align="center" width=100% position="float">
      <a :href="require('../assets/back.jpg')" target="_blank">
            <img src="../assets/back.jpg" height=440 width=102%>
        </a>
      </div>
<div align="center">
  <blockquote>        We charted interactions between characters in the world of <em>A Song of Ice and Fire</em> - both in the original books and in reader discussions.
</blockquote></div>
    <h3>What are we looking for?</h3>
    <div align="left">
      <p class=content p:first-child:first-letter>
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

    <h3>What data did we use?</h3>
    <div align="center">
      <div align="center">
              <img src="https://media.vanityfair.com/photos/53235792932cac31720001be/master/w_2560%2Cc_limit/george-rr-martin.jpg" width=130>
              </div>
              <p><br>The text from all five books in <em>A Song of Ice and Fire</em>: 7M words divided into 358 chapters.</p>
              <div align="center"> <img src="https://i.imgur.com/sdO8tAw.png" width=80></div>
              <p>Web scrape from 2015-2018 of 70K reddit posts from the book discussion subreddit (forum) <a href="https://www.reddit.com/r/asoiaf/" target="_blank"> /r/asoiaf </a> totalling 15M words.
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
        When we compare these partitions with the factions (families, political groups) in the fantasy world, it is seen mathematically that the book graph has highest correspondence, showing that the readers consider more than just geography and family when discussing the story.
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
    <h3>But what about all those words?</h3>
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
            Let us release our inner worldbuilding nerds on these character words and hope that our text data makes sense in a way we can qualitatively understand.
        </p>
        <div class="row" align="center">
            <div class="column" align="center">
                <figure>
                <img class="crop-height" src="../assets/dany_TF_wordcloud.png" style="width:80%">
                <figcaption>
                Words describing Daenerys in the Reddit discussions
                </figcaption>
                </figure>
            </div>
            <div class="column" align="center">
                <figure>
                <img class="crop-height" src="../assets/dany_TF_book.png" style="width:80%">
                <figcaption>
                Daenerys in the book
                </figcaption>
                </figure>
            </div>
        </div>
        <p>
          These possibly defining words include quite a few general words that are not that unique to the Mother of Dragons, but some interesting overlap is seen with words such as blood, dragon, lord, old, Daenerys, Tyrion.
          The Redditors might be adopting some of the word use of George R. R. Martin.
        </p>
        <p>
            However, we also see differences between the most frequent terms for Daenerys such as season, love, Aegon.
            Aegon is the name of another member of Dany's royal house who could be major contender to her claim to the throne but is mysteriously missing.

            Such a minor character, but possibly game-changing, character is perfect material for discussing intricate theories about the future course of the plot.
        </p>
           <div class="row" align="center">
            <div class="column" align="center">
                <figure>
                <img class="crop-height" src="../assets/jon_TF_wordcloud.png" style="width:80%">
                <figcaption>
                Reddit words describing Jon Snow
                </figcaption>
                </figure>
            </div>
            <div class="column" align="center">
                <figure>
                <img class="crop-height" src="../assets/jon_TF_book.png" style="width:80%">
                <figcaption>
                Snow in the five books
                </figcaption>
                </figure>
            </div>
            </div>
        <p>
          It's again hard to get a  clear picture of the properties of this character, but there is a larger diversity in names and words in the Reddit text world, which includes Jon Snow-adjacent talk of dragons and using his' family name "Stark" which he is as a bastard is not entitled to in the brutal medieval fantasy world.
          Such injustices could be the among the vocabulary details that the fans leave in fiction.
        </p>
          <div class="row" align="center">
            <div class="column" align="center">
                <figure>
                <img class="crop-height" src="../assets/tywin_TF_wordcloud.png" style="width:80%">
                <figcaption>
                The Reddit discussions of Tywin Lannister
                </figcaption>
                </figure>

            </div>
            <div class="column" align="center">
                <figure>
                <img class="crop-height" src="../assets/tywin_TF_book.png" style="width:80%">
                <figcaption>
                Tywin as he appears in the books
                </figcaption>
                </figure>
            </div>
        </div>
        <p>
        This old villain shows quite a few similarities including the names and words about his noble family: Tyrion, lord, father, Cersei, Jaime.
        Aerys, the Mad King, is apparently often discussed along with Tywin by the fans, while this is rarer in the books, signifying that the fans dwell on interesting back stories such as the battle between Tywin and the Mad King, while the fantasy world itself moves on from the horrid wars.
        </p>
        <p>
        To see more of these, go to our <router-link to="/game">word cloud guessing game</router-link> and see whether the words used by redditors are enough for you to recognize the fictional character or if it really is a little random.
        </p>
        <p>
         We end the word analysis by checking the defining words discussed above for their use during the development of the story.
         The mysterious Aegon, also the name of a historic person in the world, is used throughout the story with some pauses, while Dany's full first name that was very used on Reddit is not as frequently used in the books, except for in the end which also seems to contain more dragon action.
         She is, for example, also adressed by the title "Khaleesi" (a form of steppe queen) - a word detail that is important for the characters inside the world but is, for a reader, only used as immersion and not nocessary when communicating.
         </p>
         <p>
         Tywin Lannister's defining word "Aerys" from the Reddit discussions is much more rarely used than the generic and (in the patriarchal medieval-like society, all-important) defining word "father" extracted from the books.
         This makes sense given the natural difference in the text domains; the redditor discussion are much more analytical and focused on knowledge compared to the personal experiences and dialogue of fantasy prose.
            </p>
        </div>
      <div align="center">
      <figure>
        <a :href="require('../assets/lexical_dispersion.png')" target="_blank">
            <img src="../assets/lexical_dispersion.png" width=600>
        </a>
      <figcaption>
        Fig. 5 -
        A dispersion plot of the most frequent terms on the subreddit in describing Daenarys.
        (Click image for larger)
      </figcaption>
      </figure>
    </div>
    <h3> The character space </h3>
      <div align="left">
      <p>
      There was clearly a difference between the two social graphs and the previous discussions have found some dimensions of the differences between the two worlds.
      But can we map the worlds of the characters directly?
      </p>
      <p>
        A way to attempt this is by compressing the two complex text data sets into a collection simple points on a field.
        We do this using principal component analysis to find the most meaningful way to visualize the 34 character texts on 2D image - both for the book chapters and reddit posts.
        The result is shown below:
      </p>
      <div align="center">
      <figure>
        <a :href="require('../assets/pca_reddit.png')" target="_blank"> <!-- NOTE!: png-titlerne er omvendte! -->
            <img src="../assets/pca_reddit.png" width=900>
        </a>
      <figcaption>
        Fig. 6 -
        The character space created from the book chapters
        (Click to view big)
      </figcaption>
      </figure>
      <figure>
        <a :href="require('../assets/pca_book.png')" target="_blank">
            <img src="../assets/pca_book.png" width=900>
        </a>
      <figcaption>
        Fig. 7 -
        The 2D representation of character texts from Reddit posts
        (Click to view big)
      </figcaption>
      </figure>
      </div>
      <p>
        What can we do with the above, weird mathematical abstraction where the rich text relating to each character is suddenly reduced to an arrow?
        Well, we can look what arrows are related!
        For the book data, the arrows are divided beautifully into factions: When moving clock-wise, the first four are different cour personalitites, the next many are Lannisters, then the Baratheoons, then the Starks and Notheners.
        We then again support the idea that book co-mentions are contain much geographic and factional context.  Let's also note that, in this space, the rotten child king Joffrey is more of a Lannister than he is a Baratheon despite of his name - is a proposition that would not seem controversial to any viewer or reader.
        </p>
        <p>
        The Reddit space similarly seems influenced by the factions, but the two possible main characters Jon Snow and Dany stand out from the crowd as being unique in the text world.
        Why are these so special and why do they sit up in the corner together?
        Well, hard to answer when we don't want to directly spoil anything.
      </p>
      <p>All in all, the two worlds are clearly connected - based on the same understanding on a fictional place, but do contain information about different kinds of relationships between these fantasy people.</p>
      </div>
    <h3>Tell me yours and I'll tell you mine</h3>
    <div align="left">
    <p>
        Now that we have seen which words describe characters and how characters can be put into different communities, we want to investigate
        an even more important question: Who does Reddit have the hots for? Who does Reddit have it out for? Does Reddit - one of the most
        opinionated platforms on the planet - have characters they seem to be neutral towards? It is time to find out with the illustration below,
        showing redditor sentiment, their attitude, for five interesting characters.
    </p>
    </div>
    <div align="center">
        <img class="crop-height" src="../assets/sentiment_analysis.png" width=550>
    </div>
    <div align="left">
    <p>
    The visualization shows, using the two axes, two different measurements of the fan opinion: The VADER method is made specifically for social media text while the dictionary based Hedometer measurements looks at each word independently.
    </p>
    <p>
        Immediately, we notice that the text of some of the characters reach outside of the plot borders. A shame, but we have much more important
        results to discuss! Firstly, we see that we finally have an answer to whether the spoiled brat Joffrey or the mocking sadist Ramsay is the most hated; Reddit answers a resounding Ramsay, no matter which of the two measurements are used.
    </p>
    <p>
        Another quick point is that the VADER sentiment analysis actually gets widely different answers than the dictionary-based sentiment analysis.
        This and many more details can studied in our notebook tailor-made for this project.
        It contains all the code used to make the plots and get the results you have been enjoying throughout this website.
        Come have a look, we look forward to being shamed for using try except statements instead of handling errors like adults.
    </p>
    </div>
    <h3>What was it all about?</h3>
    <div align="left">
        <p>
        We tried to pry an understanding out of the text datasets and their differences:
        Our tools were blunt and our goals more of discussion than hard science, so no more than an intuitive understanding is expected.
        But isn't that also what sum of all those previous plots and their underlying analyses give us?
        A view into two ways to visit a fantasy world:
        One of the actual geographic relationships, another of their comparisons on a more interpretational level.
        One where families go together, another where the most unique people are connected transcending time and space.
        One of fantasy historical facts, another of opinion and preference.
        </p>
        <p>
        After working though the two text domains, we are not quite as pessimistic as John Harrison:
        Worldbuilding might learn readers the art of accepting complex fictive universes as real, but we still have hope that the search for meaningful explanations that seem to characterize the discussions ultimately make the nerdy readers better at understanding their own real life world.
        Even if that one has a shocking lack of dragons.
        </p>
        <p>
        Remember to check out <router-link to="/game"> our word cloud game </router-link> and read details at <router-link to ="/about">the about page</router-link>.
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
h1 {
    text-transform: capitalize;
    font-size: 3.6rem;
}
h3 {
    text-transform: capitalize;
    font-size: 2rem;
}
@import url(https://fonts.googleapis.com/css?family=Montserrat:700);
body{
  margin:0;
  width:100%;
  height:100vh;
  background-repeat: no-repeat;
}
svg{
  width:50%;
  height: 40%;
}
blockquote {
  font-weight: 100;
  font-size: 2rem;
  max-width: 860px;
  line-height: 1.4;
  margin: 0;
  padding: .5rem;
}

blockquote:before,
blockquote:after {
  position: absolute;
  color: #f1efe6;
  font-size: 8rem;
  width: 4rem;
  height: 4rem;
}

blockquote:before {
  content: '“';
  left: -5rem;
  top: -2rem;
}

blockquote:after {
  content: '”';
  right: -5rem;
  bottom: 1rem;
}
</style>
