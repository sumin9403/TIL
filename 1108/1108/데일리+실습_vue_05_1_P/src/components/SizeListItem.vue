<template>
  <div @click="updateSizeList" class="row" :class="{choice :size.selected}"> 
    <div class="col-6">
    {{ size.name }}
    </div>
    <div class="col-6"> {{ size.price }}원</div>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods:{
    updateSizeList() {
      this.$store.commit('updateSizeList', this.size)
    }
  }
}
</script>

<style>
.choice {
  border: 2px solid black;
 }
</style>