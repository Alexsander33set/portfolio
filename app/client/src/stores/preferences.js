import { ref, watch } from 'vue'
import { defineStore } from 'pinia'

import { useI18n } from 'vue-i18n'


export const usePreferencesStore = defineStore('preferences', () => {
  const { locale } = useI18n()
  console.log("locale: " + locale.value)

  const language = ref(locale.value)
  const acceptedLanguages = [
    {
      label:"Português Brasil",
      value:"pt_br",
      icon:"flagpack:br"
    },
    {
      label:"English",
      value:"en_us",
      icon:"flagpack:us"
    }
  ]
  function changeLanguage() {
    locale.value = language.value
  }
  watch(
    language,
    (langValue) => {
      localStorage.setItem("language", JSON.stringify(langValue))
      changeLanguage()
      console.log("watch language: " + langValue)
    },
    { deep: true}
  )

  if (localStorage.getItem("language")){
    language.value = JSON.parse(localStorage.getItem("language"))
    console.log("language localStorage: " + language.value);
  }
  else{
    let langByBrowser = (navigator.language).toLowerCase().replace("-", "_")

    acceptedLanguages.map((lang) => {
      if (lang == langByBrowser) {
        language.value = langByBrowser
      }
    })
  }


  return {
    language, acceptedLanguages
  }
})