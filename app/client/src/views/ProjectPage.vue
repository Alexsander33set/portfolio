<template>
  <div class="about">
    <h1>{{projectName}}</h1>
  </div>
</template>

<script setup>
import {} from 'vue'

import { useRoute } from 'vue-router'
const route = useRoute()

const projectName = route.params.name

</script>
