<template>
  <div class="row" @click="selectMenu" :class="{choice : menu.selected}">
    <!-- <div class="col-2 image-box"><img :  src="menu.image" class="image-thumbnail"></div> -->
    <div class="col-2">{{ menu.title }}</div>
    <div class="col-2">{{ menu.price }}</div>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods:{
    selectMenu: function () {
      this.$store.commit('updateMenuList', this.menu)
    },
  }
}
</script>

<style>
.choice {
  border: 2px solid black;
 }
</style>