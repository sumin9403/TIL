import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
      title: '아메리카노',
      price: 3000,
      selected: true,
      image: 'https://source.unsplash.com/featured/?americano'
    },
    {
      title: '라떼',
      price: 4000,
      selected: false,
      image: 'https://source.unsplash.com/featured/?latte'
    },
    {
      title: '카푸치노',
      price: 4500,
      selected: false,
      image: 'https://source.unsplash.com/featured/?capuccino'
    },
  ],
  // small medicum, large
    sizeList: [{
      name: 'small',
      price: 0,
      selected: true
    },
    {
      name: 'medium',
      price: 500,
      selected: false
    },
    {
      name: 'large',
      price: 1000,
      selected: false
    },
  ],
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state) {
      const totalPrice = state.orderList.reduce((total, elem) => {
        return total + elem.menu.price + elem.size.price
      }, 0)
      return totalPrice
    },
    // totalPrice(state) {

    // }


  },
  mutations: {
    addOrder: function (state) {

      let menu, size
      // console.log(state.menuList[1])
      for (let i=0; i<3; i++){
        if (state.menuList[i].selected){
          menu = state.menuList[i]
          state.menuList[i].selected = false
        }
        if (state.sizeList[i].selected){
          size = state.sizeList[i]
          state.sizeList[i].selected = false
         
        }
      }
      const order = {
        menu,
        size,
      }
      state.orderList.push(order)
      console.log(order)

      state.menuList[0].selected = true
      state.sizeList[0].selected = true
    },

    updateMenuList: function (state, selectedMenu) {
      const newMenuList = state.menuList.map((elem) => {
        if (selectedMenu === elem) {
          elem.selected = !elem.selected
        } else {
          elem.selected = false
        }
        return elem
    })
      state.menuList = newMenuList
    },
    updateSizeList: function (state, selectedSize) {
      const newSizeList = state.sizeList.map((elem) => {
        if (selectedSize == elem) {
          elem.selected = !elem.selected
        }
        else {
          elem.selected = false
        }
        return elem
      })
      state.sizeList = newSizeList
    },
  },
  actions: {
  },
  modules: {
  }
})