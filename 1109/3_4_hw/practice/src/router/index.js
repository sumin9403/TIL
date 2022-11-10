import Vue from 'vue'
import VueRouter from 'vue-router'
import First from '../views/First.vue'
import Second from '../views/Second.vue'

Vue.use(VueRouter)

const routes = [
  
  {
    name: 'first',
    path: '/',
    component: First,
  },
  {
    name:'Second',
    path:'/second',
    component: Second,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
