<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import ProjectList from '@/components/ProjectList.vue'

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

function getProjects(){
  axios.get("/api/projects")
    .then((res)=>{
      console.log(res)
      projects.value = res.data
  })
}
</script>

<template>
  <main>
    <hr>
    <h1 align="center">Meu Portfólio</h1>
    <Button @click="getProjects" variant="outline" class="m-4">Obter projetos</Button>
    <hr>
    <ProjectList :projects="projects" :title="$t('projects.title')" />
  </main>
</template>
