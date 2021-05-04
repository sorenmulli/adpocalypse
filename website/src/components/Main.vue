<template>
  <div class="home">
    <h1>{{ msg }}</h1>
    <p>
        We charted interactions between characters in the world of <em>A Song of Ice and Fire</em> - both in the original books and in reader discussions.
    </p>
    <p>
        Here's what we found!
    </p>
   </div>
    <!--Guessing game-->
    <h3> Guess characters from Reddit discussion word clouds  </h3>
    <div v-if="started">
        <form @submit.prevent="submit">
            <div>
                <p> What character are the readers discussing here? </p>
                <p> "DRAGON MOMMY" </p>
            </div>
            <div>
            <select v-model="selected">
                <option value="" disabled>Pick one</option>
                <option v-for="option in options" :value="option.value" :key="option.index">
                    {{ option.text }}
                </option>
            </select>
            <button type="submit">Guess</button>
            </div>
        </form>
        <p> {{resultMsg}} </p>
  </div>
  <div v-else>
    <p> Do you think you know the characters? See if you can recognize them in the reader discussions!</p>
    <button type="button" @click="start">Start guessing</button>
  </div>
  <!--Video-->
  <div>
    <h3> Introductionary video </h3>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/NAvDzTBnw3s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
    </iframe>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Home',
  props: {
    msg: String
  },
  data () {
    return {
      started: false,
      rightAnswer: 'D',
      options: [
        { text: 'Daenarys', value: 'D' },
        { text: 'Jon Snow', value: 'J' }
      ],
      selected: '',
      resultMsg: ''
    }
  },
  methods: {
    start () {
      this.started = true
    },
    submit () {
      this.resultMsg = this.selected === this.rightAnswer ? 'You got that one right!' : 'Nope, try another'
    }
  }
})
</script>

<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
