import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomePage.vue'
import AboutView from '../views/AboutPage.vue'
import ProjectPage from '../views/ProjectPage.vue'
import PrivacyandAcceptanceTerms from '../views/PrivacyandAcceptanceTerms.vue'
import AdminPage from '../views/AdminPage.vue'
import LoginPage from '../views/LoginPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/project/:name',
      name: 'project page',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: ProjectPage
    },
    {
      path: '/:language/privacy-&-acceptance-terms',
      name: 'Privacy and Acceptance Terms',
      component: PrivacyandAcceptanceTerms
    },
    {
      path: '/admin',
      name: 'Admin',
      component: AdminPage,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginPage
    },
    { path: '/:pathMatch(.*)*', redirect: '/' }
  ]
})

export default router
