import { ref, watch } from 'vue'
import { defineStore } from 'pinia'

import { useI18n } from 'vue-i18n'


export const preferences = defineStore('preferences', () => {
  const { locale } = useI18n()
  
  const language = ref(locale.value)
  const acceptedLanguages = [
    {
      label:"Português Brasil",
      value:"pt_br"
    },
    {
      label:"English",
      value:"en_us"
    }
  ]

  if (localStorage.getItem("language")){
    language.value = JSON.parse(localStorage.getItem("language"))
    locale.value = JSON.parse(localStorage.getItem("language"))
    console.log("OPA, tem coisa de language: " + language.value);
  }else{
    let PrefLangByNavigator = (navigator.language).toLowerCase()

    acceptedLanguages.map((language) => {
      if (language.value == PrefLangByNavigator) {
        language.value = PrefLangByNavigator
        locale.value = PrefLangByNavigator
      }
    })
  }
  watch(
    language,
    (languageValue) => {
      localStorage.setItem("language", JSON.stringify(languageValue))
    },
    { deep: true}
  )

  function toggleLanguage(i18n, newValue) {
    if (i18n.availableLocales.includes(newValue)) {
      try {
        i18n.locale = newValue
        language.value = newValue
        console.log('language changed to: '+i18n.locale)
      } catch (error) {
        console.error(error);
      } 
    }
  }




  return {
    language, acceptedLanguages, toggleLanguage
  }
})