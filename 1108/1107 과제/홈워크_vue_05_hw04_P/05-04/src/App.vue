<template>
  <div id="app">
    <h2>Counter: {{ counter }}</h2>
    <h2>Counter x2: {{ counterDouble }}</h2>
    <button @click="increase">increase +</button><button @click="decrease">decrease -</button>
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {
  },
  data: function() {
    return {
    }
  },
  computed:{
    counter () {
      return this.$store.state.counter
    },
    counterDouble() {
      return this.$store.getters.counterDouble
    }
  },
  methods: {
    increase() {
      this.$store.commit('increase')
    },
    decrease() {
      this.$store.commit('decrease')
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
