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
  <div id="project-list-container">
    <h2 class="text-lg font-bold my-4" v-if="title">{{ title }}</h2>
    <div class="flex flex-col gap-4">

      <div v-for="(project, index) in props.projects" :key="index"
        class="shadow-[0_0px_3px_0px_rgba(0,0,0,0.3)] p-4 rounded-md">
        <h3>{{ project.name }}</h3>
        <p>{{ project.description }}</p>
        <p>Tecnologias: {{ project.technologies.join(', ') }}</p>
        <div class="flex gap-2 mt-4">
          <a :href="'https://' + project.github" target="_blank" rel="noopener noreferrer"
          v-if="!project.is_private"
          class="w-full">
            <Button variant="outline">{{ $t('projects.github') }}</Button>
          </a>
          <a :href="'https://' + project.url" target="_blank" rel="noopener noreferrer">
            <Button variant="outline">{{ $t('projects.view') }}</Button>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
