import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import WeatherHome from '../views/WeatherAPI/Homepage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    meta: { title: 'Skills - MyApp' },
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/weatherAPI',
    name: 'WeatherHome',
    meta: { title: 'Skills - MyApp' },
    component: WeatherHome
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
