<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import { Icon } from '@iconify/vue'

import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'

const devEnvAlert = ref(true)
const setDevEnvAlert = () => {
  console.log("setDevEnvAlert called")
  devEnvAlert.value = !devEnvAlert.value
  localStorage.setItem('devEnvAlert', JSON.stringify(devEnvAlert.value))
}
if (localStorage.getItem('devEnvAlert')){
  devEnvAlert.value = JSON.parse(localStorage.getItem('devEnvAlert'))
}


import ProjectList from '@/components/ProjectList.vue'

const TOFisOpen = ref(false)
const projects = ref([])

function getProjects(){
  try{
    let response = axios.get("/api/projects")
    let {data, headers, status} = response

    if (status == 200 || headers['content-type'] == "application/json"){
      projects.value = data
    } else {
      console.warn(">> Invalid Request <<")
      projects.value = null
    }
  } catch (err) {
    console.error(err)
    // projects.value = null
    projects.value = projectsMockup
  }
}

/** mockup */
const projectsMockup = [
    {
        "_id": "66baecd6ed46e383b86a5484",
        "name": "Weather Forecast",
        "slug": "weather-forecast",
        "description": "something",
        "technologies": [
            "java",
            "node",
            "python"
        ],
        "url": "www.apfs.com.br",
        "is_private": false,
        "created_at": 1723526343.82374
    },
    {
        "_id": "66baf3812ffa799538467a33",
        "name": "Weather Forecast",
        "slug": "weather-forecast",
        "description": "something",
        "technologies": [
            "java",
            "node",
            "python"
        ],
        "url": "www.apfs.com.br",
        "is_private": false,
        "created_at": 1723528060
    },
    {
        "_id": "66baf3b55b1172f323a2cc99",
        "name": "Weather Forecast",
        "slug": "weather-forecast",
        "description": "something",
        "technologies": [
            "java",
            "node",
            "python"
        ],
        "url": "www.apfs.com.br",
        "is_private": false,
        "created_at": 1723528108
    }
]

getProjects()
console.log(projects.value)
</script>

<template>
  <main class="relative scroll-smooth scroll-pt-12 flex-1 dark:text-gray-100">
    <section id="temp" v-if="devEnvAlert" class="container mt-2 -mb-4">
      <Alert>
        <Icon icon="mdi:alert-circle-outline" class="w-4 h-4"/>
        <AlertTitle>
          Application under development
          <Button class="float-right" variant="outline" size="icon" @click="setDevEnvAlert()">
            <Icon icon="mdi:close" class="w-4 h-4"/>
          </Button>
        </AlertTitle>
        <AlertDescription>
          This application is under development and may not work as expected.
        </AlertDescription>
      </Alert>
    </section>
    <section id="presentation" class="mt-16 container flex flex-col justify-center relative">
      <h1 class="font-semibold tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">Alexsander Patrick Ferreira Santos</h1>
      <h2 class="text-2xl mt-1">{{ $t('presentation.subtitle') }}</h2>
      <p class="py-4 mb-4 w-1/2 text-lg font-normal text-gray-500 dark:text-gray-400">
        {{ $t('presentation.description') }}
      </p>
    </section>

    <section id="skills" class="container mt-12">
      <h2 class="text-xl">{{ $t('skills.title') }}</h2>
      <div class="flex flex-wrap gap-4 items-center mt-4 text-gray-700 dark:text-gray-100">
        <article class="flex items-center gap-2 py-4 px-8 text-lg rounded-sm border hover:scale-105 transition-transform">
            <Icon icon="mdi:eye-outline" /> {{ $t('skills.list.accessibility') }}
        </article>
        <article class="flex items-center gap-2 py-4 px-8 text-lg rounded-sm border hover:scale-105 transition-transform">
            <Icon icon="mdi:shield-check-outline" /> {{ $t('skills.list.security') }}
        </article>
        <article class="flex items-center gap-2 py-4 px-8 text-lg rounded-sm border hover:scale-105 transition-transform">
            <Icon icon="mdi:server" /> {{ $t('skills.list.devops') }}
        </article>
      </div>
      <p class="text-base mt-4">{{ $t('skills.description') }}</p>
    </section>

    <ProjectList v-if="projects" id="projects" class="container mt-12"
      :projects="projects"
      :title="$t('projects.title')" />


    <section id="contacts" class="mt-12 container grid items-center">
      <h2 class="text-xl text-center">{{ $t('contacts.title') }}</h2>
      <span class="flex justify-center gap-2 mt-2">
        <a href="https://www.linkedin.com/in/alexsander-patrick-ferreira-santos-5ba0841ba/" target="_blank">
          <Button variant="outline" class="m-2">
            <Icon icon="fa6-brands:linkedin" />
            &nbsp;Linkedin
          </Button>
        </a>
        <a href="https://github.com/Alexsander33set" target="_blank">
          <Button variant="outline" class="m-2">
              <Icon icon="fa6-brands:github" />
              &nbsp;GitHub
          </Button>
        </a>
        <a href="mailto:alexsander.patrick@gmail.com" target="_blank">
          <Button variant="outline" class="m-2">
              <Icon icon="mdi:mail" />
              &nbsp;Email
          </Button>
        </a>
      </span>
    </section>

    <div class="absolute top-20 -right-2 hover:-right1 p-2 hover:scale-105 cursor-pointer border rounded-sm text-center duration-300 hover:shadow-md opacity-50 hover:opacity-100 transition-all"
      @click="TOFisOpen = !TOFisOpen"
      @mouseleave="TOFisOpen = false"
    >
      <Icon icon="mdi:menu-left" class="scale-150 transition-all duration-300" :class="{'rotate-180': TOFisOpen}" />
      <div id="tableOfContents" v-if="TOFisOpen"
        class="flex flex-col gap-2 text-muted-foreground transition-all mt-2">
        <a href="#presentation" class="hover:text-primary hover:underline transition-colors">{{ $t('tableOfContents.presentation') }}</a>
        <a href="#projects" class="hover:text-primary hover:underline transition-colors">{{ $t('tableOfContents.projects') }}</a>
        <a href="#contacts" class="hover:text-primary hover:underline transition-colors">{{ $t('tableOfContents.contacts') }}</a>
      </div>
    </div>
  </main>
</template>

<style scoped>
#tableOfContents {
  animation: slideIn 0.5s ease-in-out forwards;
}

@keyframes slideIn {
  from {
    width: 0;
    opacity: 0;
  }
  to {
    width: 150px;
    opacity: 1;
  }
}
</style>