<script setup>
import axios from 'axios'
import { ref } from 'vue'

const response = ref([])

function getProjects(){
  axios.get("/api/projects")
    .then((res)=>{
      console.log(res)
      response.value = res
  })
}
</script>

<template>
  <main>
    <hr>
    <h1 align="center">My Portfolio</h1>
    <button @click="getProjects">Botão</button>
    <hr>
    <h3>Body</h3>
    {{ response }}
  </main>
</template>
