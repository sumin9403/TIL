<template>
  <div id="app" style="background-color: ;">
    <div >
    <h1 class="text-center">Coffee Order App</h1>
    <div class="row bg-secondary">
      <div class="col-6 bg-white">
        <MenuList/>
      </div>
      <div class="col-6 bg-white">
        <SizeList/>
      </div>
    </div>
    <br>
    <div class="row">
    <button class="col-12" @click="addOrder">장바구니 담기</button>
    <OrderList />
    </div>
  </div>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList';
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'

export default {
  name: 'App',
  components:{
    MenuList,
    SizeList,
    OrderList,
  },
  methods:{
    addOrder: function () {
      this.$store.commit('addOrder')
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
</style>
