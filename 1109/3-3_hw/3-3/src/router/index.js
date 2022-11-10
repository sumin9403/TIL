import Vue from 'vue'
import VueRouter from 'vue-router'
import Nocolor from '../views/Nocolor.vue'
import Ssafling from '../views/Ssafling.vue'
import Ssafleaf from '../views/Ssafleaf.vue'
import Ssaflower from '../views/Ssaflower.vue'
import Not_found from '../views/404.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/Nocolor',
    name: 'nocolor',
    compoment: Nocolor
  },
  {
    path: '/ssafling',
    name: 'ssafling',
    compoment: Ssafling
  },
  {
    path: '/ssafleaf',
    name: 'ssafleaf',
    compoment: Ssafleaf
  },
  {
    path: 'ssaflower',
    name: 'ssaflower',
    compoment: Ssaflower
  },
  {
    path: 'not_found',
    name: 'not_found',
    compoment: Not_found
  },
  {
    path: '*',
    redirect: { name:'not_found' }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
