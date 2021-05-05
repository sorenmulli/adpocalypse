<template>
  <div class="home">
    <h1>{{ msg }}</h1>
    <p>
        We charted interactions between characters in the world of <em>A Song of Ice and Fire</em> - both in the original books and in reader discussions.
    </p>
    <p>
        Here's what we found!
    </p>

    <h2>Which character are most often mentioned together?</h2>
    <h3>What did we do and how?</h3>
    <p>
        We used community detection on the 34 most notable characters of Game of Thrones on both the books and on reddit. This will allow us to see if redditors prioritize the character relations in the same way as the books do and if characters are usually mentioned in relation to their factions, like one might expect. The result of this analysis can be seen in the four pictures below. The two first pictures are the communities found in the book and on reddit respectively. The two next pictures are how one might expect the communities to look if characters were only mentioned along with other characters from the same faction.
    </p>
    <img src="../assets/communities_book.png">
    <img src="../assets/communities_true_book.png">
    <img src="../assets/communities_reddit.png">
    <img src="../assets/communities_true_reddit.png">
    <p>
        Now these plots are interesting! The characters that have been linked are the ones that are most often mentioned together. Every character is mentioned to some extent, so these illustrations only show the MOST mentioned characters. Now what do we see from these illustrations?
        Well, in the graph of the book mentions, we see that the Starks and Lannisters are mentioned together like expected and as can be seen in the true graph.
    </p>

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
