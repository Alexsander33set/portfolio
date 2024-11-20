<script setup>
import { defineProps } from 'vue'
import { RouterLink } from 'vue-router'

import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { Icon } from '@iconify/vue'

const props = defineProps({
  projects: {
    type: Array,
    required: true
  },
  title: {
    type: String,
    default: 'Projetos'
  }
})

const filter = {
"html":"nonicons:html-16",
"css":"nonicons:css-16",
"javascript":"nonicons:javascript-16",
"typescript":"nonicons:typescript-16",
"node":"nonicons:node-16",
"vue":"nonicons:vue-16",
"vuejs":"nonicons:vue-16",
"vue3":"nonicons:vue-16",
"python":"nonicons:python-16",
"flask":"devicon:flask",
"java": ":nonicons:java-16",
"angular": "nonicons:angular-16",
"tailwind": "devicon:tailwindcss",
"tailwindcss": "devicon:tailwindcss",
"eslint": "nonicons:eslint-16",
"prettier": "nonicons:prettier-16",
"aws": "vscode-icons:file-type-aws",
"yaml": "vscode-icons:file-type-aws",
"yarn": "devicon:yarn",
"vite": "devicon:vitejs",
"vuetify": "devicon:vuetify",
"supabase": "devicon:supabase",
"sonarqube": "devicon:sonarqube",
"railway": "devicon:railway",
"mongodb": "devicon:mongodb"
}
</script>

<template>
  <div id="project-list-container">
    <h2 class="my-4 text-xl" v-if="title">{{ title }}</h2>
    <div class="flex flex-col gap-4">

      <template v-if="projects.length > 0">
        <div v-for="(project, index) in props.projects" :key="index"
        class="shadow-[0_0px_3px_0px_rgba(127,127,127,0.5)] p-4 rounded-md">
          <h3 class="text-lg capitalize">
            {{ project.name }}
          </h3>
          <p class="mt-2 whitespace-pre-wrap line-clamp-2"
            v-html="project.description">
          </p>
          <div class="flex gap-2 mt-2">
            <Badge class="capitalize leading-normal inline-flex gap-2"
              v-for="(tech, i) in project.technologies"
              :key="i">
              <Icon v-if="filter[tech]" :icon="filter[tech]" />
              {{ tech }}
            </Badge>
          </div>

          <div class="flex justify-start gap-2 mt-6">
            <RouterLink :to="'/project/'+project.slug">
              <Button variant="outline">
                {{ $t('projects.view') }}
              </Button>
            </RouterLink>
            <template v-if="!project.is_private">
              <a v-if="project.github" :href="project.github" target="_blank" rel="noopener noreferrer">
                <Button variant="outline"><Icon icon="mdi:github" /></Button>
              </a>
            </template>
            <a v-if="project.url" :href="project.url" target="_blank" rel="noopener noreferrer">
              <Button variant="outline"><Icon icon="akar-icons:globe" /></Button>
            </a>
          </div>
        </div>
      </template>
      <template v-else>
        <div class="shadow-[0_0px_3px_0px_rgba(0,0,0,0.3)] p-4 rounded-md">
          <h3>project.name</h3>
          <p> project.description </p>
          <p>Tecnologias:  project.technologies.join(', ') </p>
          <div class="flex gap-2 mt-4">
            <a href="#" target="_blank" rel="noopener noreferrer" class="w-full">
              <Button variant="outline"> projects.github </Button>
            </a>
            <a href="#" target="_blank" rel="noopener noreferrer">
              <Button variant="outline"> projects.view </Button>
            </a>
        </div>
      </div>
      </template>
    </div>
  </div>
</template>
