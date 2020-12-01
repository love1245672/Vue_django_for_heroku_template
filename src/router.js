import Vue from 'vue'
import Router from 'vue-router'
import Show_All from '@/components/Show_All'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Show_All',
      component: Show_All
    },
  ]
})
