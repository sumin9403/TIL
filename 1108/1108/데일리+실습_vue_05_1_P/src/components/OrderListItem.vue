<template>
  <li>
    {{ order.menu.title }}
    {{ order.size.name }}
    <p>{{totalPrice}} 원</p>
    <hr>
  </li>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    totalPrice: function () {
      return this.order.menu.price + this.order.size.price
    },
  },
}
</script>

<style>
</style>