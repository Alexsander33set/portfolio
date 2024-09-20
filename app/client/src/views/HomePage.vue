<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import { Icon } from '@iconify/vue'
import ProjectList from '@/components/ProjectList.vue'

/** mockup */
const projects = ref([
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
])

const TOFisOpen = ref(false)

function getProjects(){
  axios.get("/api/projects")
    .then((res)=>{
      console.log(res)
      projects.value = res.data
  })
}

// 
try {
  getProjects()
} catch (error) {
  console.error(error)
}
</script>

<template>
  <main class="relative scroll-smooth scroll-pt-12 overflow-x-hidden">
    <section id="presentation" class="pt-20 container flex flex-col justify-center relative">
      <h1 class="text-4xl text-4xl font-bold dark:text-white">Alexsander Patrick Ferreira Santos</h1>
      <h2 class="text-xl">{{ $t('presentation.subtitle') }}</h2>
      <p class="py-4 mb-4 w-1/2 text-lg font-normal text-gray-500 dark:text-gray-400">
        {{ $t('presentation.description') }}
      </p>
    </section>

    <section id="skills" class="container">
      <h2 class="text-xl">{{ $t('skills.title') }}</h2>
      <div class="flex flex-wrap gap-2 items-center mt-4 text-gray-700">
        <article class="flex items-center gap-2 py-2 px-4 text-lg rounded-sm border">
            <Icon icon="mdi:eye-outline" /> {{ $t('skills.list.accessibility') }}
        </article>
        <article class="flex items-center gap-2 py-2 px-4 text-lg rounded-sm border">
            <Icon icon="mdi:shield-check-outline" /> {{ $t('skills.list.security') }}
        </article>
        <article class="flex items-center gap-2 py-2 px-4 text-lg rounded-sm border">
            <Icon icon="mdi:server" /> {{ $t('skills.list.devops') }}
        </article>
      </div>
      <p class="text-xl mt-4">{{ $t('skills.description') }}</p>
    </section>

    <ProjectList id="projects" class="container"
      :projects="projects"
      :title="$t('projects.title')" />

    <section id="contacts" class="mt-12 container flex flex-col items-center justify-center">
      <h2>{{ $t('contacts.title') }}</h2>
      <div class="flex gap-2">
        <a href="https://www.linkedin.com/in/alexsander-patrick-ferreira-santos-5ba0841ba/" target="_blank">
          <Button variant="outline" class="m-2">
              <Icon icon="fa6-brands:linkedin" />
            &nbsp;Alexsander Patrick Ferreira Santos
          </Button>
        </a>
        <a href="https://github.com/Alexsander33set" target="_blank">
          <Button variant="outline" class="m-2">
              <Icon icon="fa6-brands:github" />
              &nbsp;Alexsander33set
          </Button>
        </a>
      </div>
    </section>

    <div class="absolute top-20 -right-4 hover:-right-2 p-2 hover:scale-105 cursor-pointer border rounded-sm text-center duration-300 hover:shadow-md opacity-50 hover:opacity-100 transition-all"
      @click="TOFisOpen = !TOFisOpen" @mouseleave="TOFisOpen = false"
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