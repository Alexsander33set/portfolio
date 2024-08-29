<script setup>
import { defineProps } from 'vue'
import { Button } from '@/components/ui/button'

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
</script>

<template>
  <div class="project-list-container">
    <h2 v-if="title">{{ title }}</h2>
    <div class="project-list">
      <div v-for="project in projects" :key="project._id.$oid" class="project-item">
        <h3>{{ project.name }}</h3>
        <p>{{ project.description }}</p>
        <p>Tecnologias: {{ project.technologies.join(', ') }}</p>
        <a :href="'https://'+project.url" target="_blank" rel="noopener noreferrer">
          <Button variant="outline">{{ $t('projects.view') }}</Button>
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
.project-list-container {
  margin-top: 1rem;
}

.project-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.project-item {
  border: 1px solid #ccc;
  padding: 1rem;
  border-radius: 8px;
}
</style>