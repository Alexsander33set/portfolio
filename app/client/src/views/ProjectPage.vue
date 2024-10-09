<script setup>
import axios from 'axios';
import { ref } from 'vue'

import { useRoute } from 'vue-router'
const route = useRoute()

import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from '@/components/ui/breadcrumb'
import { Badge } from '@/components/ui/badge'
import { Icon } from '@iconify/vue'



const projectName = route.params.name

function getProjects(){
  axios.get(`/api/project?${projectName}`)
    .then((res)=>{
      console.log(res)
      return res
  })
}
// Example
const project = ref(
  {
    name: "Weather Forecast",
    slug: "weather-forecast",
    description: "something",
    technologies: ["java", "node", "python"],
    url: "www.apfs.com.br",
    is_private: false,
    created_at: new Date()
  }
)

// const project = getProjects()

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
"supabase": "devicon:supabase",
"sonarqube": "devicon:sonarqube",
"railway": "devicon:railway",
"mongodb": "devicon:mongodb"
}
</script>

<template>
  <main class="p-8 min-h-dvh">
    <Breadcrumb>
      <BreadcrumbList>
        <BreadcrumbItem>
          <BreadcrumbLink href="/">
            home
          </BreadcrumbLink>
        </BreadcrumbItem>
        <BreadcrumbSeparator />
        <BreadcrumbItem>
          <BreadcrumbLink href="/projects">
            projects
          </BreadcrumbLink>
        </BreadcrumbItem>
        <BreadcrumbSeparator />
        <BreadcrumbItem>
          <BreadcrumbPage>{{ projectName }}</BreadcrumbPage>
        </BreadcrumbItem>
      </BreadcrumbList>
    </Breadcrumb>
    <section id="proj-presentation" class="flex gap-6 pt-6">
      <div id="proj-image" class="rounded-lg overflow-hidden shadow-md">
        <img src="https://picsum.photos/300/200">
      </div>
      <div id="proj-main-text">
        <div id="proj-title-&-privace" class="inline-flex gap-4">
          <h3 class="text-3xl capitalize">
            {{project.name}}
          </h3>
          <Badge  variant="outline">
            {{ project.is_private? "Private" : "Public" }}
          </Badge>
          <Badge  variant="outline">
            {{ project.status? "Active" : "Inative" }}
          </Badge>
        </div>
        <div id="proj-link" class="text-purple-500 text-primary leading-loose">
          <a :href="project.url" target="_blank" rel="noopener noreferrer">{{project.url}}</a>
        </div>
        <div id="proj-creation-date" class="leading-loose">
          Created at {{ project.created_at.toLocaleDateString(undefined,{
            month: 'short',
            year:'2-digit'
          })}}
        </div>
      </div>
    </section>
    <section id="technologies" class="pt-4">
      <h4 class="text-xl">Technologies</h4>
      <div class="pt-2 inline-flex gap-2">
        <Badge class="capitalize leading-normal inline-flex gap-2" 
          v-for="(tech, i) in project.technologies" 
          :key="i">
          <Icon :icon="filter[tech]" class="" />
          {{ tech }}
        </Badge>
      </div>
    </section>
    <section id="proj-description" class="pt-4">
      <h4 class="text-xl">Description</h4>
      <div class="prose lg:prose-xs">
        {{ project.description }}
      </div>
      
    </section>
  </main>
</template>