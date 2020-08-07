import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Api from './views/Api.vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'

Vue.use(Router)
Vue.use(Buefy)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    }
  ]
})
