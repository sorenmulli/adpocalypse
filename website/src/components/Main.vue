<template>
  <div class="home">
    <h1>{{ msg }}</h1>
    <p>
        We charted interactions between characters in the world of <em>A Song of Ice and Fire</em> - both in the original books and in reader discussions.
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
