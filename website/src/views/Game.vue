<template>
  <div class="game">
    <h1> Guess characters from Reddit discussion word clouds  </h1>
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
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'Game',
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
