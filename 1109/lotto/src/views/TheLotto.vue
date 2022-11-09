<template>
    <div class="lotto">
      <h1>로또</h1>
      <button @click="getNumbers">Get Lucky Numbers</button>
      <p v-show="pick">{{ numbers }}</p>
    </div>
  </template>

<script>

import _ from 'lodash'
export default {
    name: 'TheLotto',
    data() {
        return {
            numbers: null,
            pick: false,
        }
    },
    methods: {
        getNumbers(){
            this.numbers = _.sampleSize(_.range(1,46), 6)
            this.pick = true
        },
    },
    computed: {

    }

}
</script>