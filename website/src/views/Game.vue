<template>
  <div class="game">
    <h1> Guess characters from Reddit discussion word clouds  </h1>
    <div v-if="started">
        <form @submit.prevent="submit">
            <div>
                <p> What character are the readers discussing here? </p>
                <img :src="wordCloud" width=900>
            </div>
            <div>
            <select v-model="selected">
                <option value="" disabled>Pick one</option>
                <option v-for="option in options" :value="option" :key="option.index">
                    {{ option }}
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
import { useMeta } from 'vue-meta'

import guessGame from '../assets/guessGame.json'

export default defineComponent({
  name: 'Game',
  setup () {
    useMeta({ title: 'Game' })
  },
  data () {
    return {
      started: false,
      options: Object.keys(guessGame),
      rightAnswer: '',
      selected: '',
      resultMsg: '',
      wordCloud: ''
    }
  },
  methods: {
    start () {
      this.selected = ''
      this.rightAnswer = this.options[Math.floor(Math.random() * this.options.length)]
      this.wordCloud = require('../assets/' + guessGame[this.rightAnswer])
      console.log(this.rightAnswer)

      this.started = true
    },
    submit () {
      const correct = this.selected === this.rightAnswer
      if (correct) {
        this.resultMsg = 'You got that one right!'
        this.start()
      } else {
        this.resultMsg = 'Nope, try another'
      }
    }
  }
})
</script>
