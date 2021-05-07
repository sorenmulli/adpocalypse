<template>
  <div class="game">
    <h1> Guess characters from Reddit discussion word clouds  </h1>
    <div v-if="started">
        <form v-if="thereIsMore" @submit.prevent="submit">
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
        <p> {{ resultMsg }} </p>
            <p v-if="total">
              Bulls-eyes: {{ corrects }}/{{ total }}
            </p>
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
      thereIsMore: true,
      options: Object.keys(guessGame),
      corrects: 0,
      total: 0,
      rightAnswer: '',
      selected: '',
      resultMsg: '',
      wordCloud: ''
    }
  },
  methods: {
    start () {
      this.started = true
      this.nextRound()
    },
    nextRound () {
      this.selected = ''
      this.rightAnswer = this.options[Math.floor(Math.random() * this.options.length)]
      console.log(this.rightAnswer)
      this.wordCloud = require('../assets/' + guessGame[this.rightAnswer])
    },
    submit () {
      const correct = this.selected === this.rightAnswer
      if (correct) {
        this.resultMsg = '🔥🐲 You got that one right! 🐲🔥'
        this.corrects++
      } else {
        this.resultMsg = '❄️☠️ No, it was actually ' + this.rightAnswer + '. Keep it up! ☠️❄️'
      }
      const rightIndex = this.options.indexOf(this.rightAnswer, 0)
      this.total++
      this.options.splice(rightIndex, 1)
      if (this.options === undefined || this.options.length === 0) {
        this.endGame()
      } else {
        this.nextRound()
      }
    },
    endGame () {
      this.thereIsMore = false
      const percentage = Math.round(this.corrects / this.total * 100)
      this.resultMsg = `🌟Game ended! You got ${percentage}% correct. Wow. Just wow. Reload page to play again! 🌟`
    }
  }
})
</script>
