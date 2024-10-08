import './assets/index.css'
import { languages } from './locales'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createI18n } from 'vue-i18n'

const i18n = createI18n({
  locale: 'pt_br',
  fallbackLocale: 'en_us',
  messages: languages,
  legacy: false,
})

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(i18n)

app.mount('#app')
