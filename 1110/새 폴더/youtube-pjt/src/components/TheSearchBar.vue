<template>
  <div>
    <input type="text" @keyup.enter="inputChange">
  </div>
</template>

<script>
export default {
    name: 'TheSearchBar',
    data () {
        return {
        }
    },
    methods: {
        inputChange(event) {
            this.$emit('input-change', event.target.value)
        }
    }

}
</script>

<style>

</style>