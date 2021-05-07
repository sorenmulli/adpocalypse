<template>
  <metainfo>
    <template v-slot:title="{ content }">{{ content ? `${content} | A Graph of Thrones` : `A Graph of Thrones` }}</template>
  </metainfo>
  <app-header />
  <router-view/>
  <app-footer />
</template>

<script>
import AppHeader from '@/components/AppHeader.vue'
import AppFooter from '@/components/AppFooter.vue'
import { useMeta } from 'vue-meta'

export default {
  components: {
    AppHeader,
    AppFooter
  },
  // eslint-disable-next-line
  setup () {
    useMeta({
      title: '',
      htmlAttrs: { lang: 'en' }
    })
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
p {
  line-height:1.5em;
  margin: 14px 20% 14px 20%;
}
a {
  color: #42b983;
}
</style>
