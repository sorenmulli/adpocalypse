<template>
    <header>
    <router-link to="/">
        <img alt="Graph Of Thrones" src="https://fontmeme.com/permalink/210428/7464690d81ebde4bf9006cfe4deedb23.png" height="50">
    </router-link>
    <p>A Song of Ice and Network Science</p>
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/game">Game</router-link></li>
        <li><router-link to="/about">About</router-link></li>
      </ul>
    </nav>
    </header>
</template>

<style lang="scss">
  header {
    display: flex;
    border-bottom: 1px solid #ccc;
    padding: .5rem 1rem;

    p {
      margin-left: 1rem;
    }
  }

  nav {
    margin-left: auto;

    ul {
      list-style: none;
    }

    ul li {
      display: inline-flex;
      margin-left: 1rem;
    }
  }
</style>
