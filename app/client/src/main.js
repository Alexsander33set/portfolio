import './assets/main.css'
import { languages } from './locales'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createI18n } from 'vue-i18n'

const i18n = createI18n({
  locale: 'pt-br',
  fallbackLocale: 'en-us',
  messages: languages
})

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(i18n)

app.mount('#app')
