<template>
  <div class="home">
    <Main msg="How did the YouTube community react to the Adpocalypse?"/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Main from '@/components/Main.vue' // @ is an alias to /src

export default defineComponent({
  name: 'Home',
  components: {
    Main
  }
})
</script>
