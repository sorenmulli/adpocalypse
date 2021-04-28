<template>
  <div class="home">
    <Main msg="How do fantasy universes look in the minds of readers?"/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Main from '@/components/Main.vue' // @ is an alias to /src
import { useMeta } from 'vue-meta'

export default defineComponent({
  name: 'Home',
  setup () {
    useMeta({ title: 'Presentation' })
  },
  components: {
    Main
  }
})
</script>
