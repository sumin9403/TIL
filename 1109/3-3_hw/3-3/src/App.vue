<template>
  <div id="app">
    <nav>
      <!-- <div @click="goNocolor">start</div> -->
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  el: 'app',
  name: 'App',
  methods:{
    // goNocolor() {
    //   this.$router.push({name: 'nocolor'})
    // }
  }

}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
