<template>
  <div>
    <h1>점심메뉴</h1>
    <button
    @click="pickLunch"
    >Pick Lunch</button>
    <p v-show="menu">{{ menu }}</p>
    <br>
    <h1>로또를 뽑아보자</h1>
    <button @click="goToLotto">Pick Lotto</button>
  </div>
</template>


<script>

import _ from 'lodash'
export default {
    name: 'LunchView',
    data() {
        return {
            menu: null
        }
    },
    methods: {
        pickLunch(){
            this.menu = _.sample(this.menus)
        },
        goToLotto() {
            this.$router.push({ name:'lotto' })
        }
    },
    computed: {
        menus() {
            return this.$store.state.menus
        } 
    }

}
</script>

<style>

</style>