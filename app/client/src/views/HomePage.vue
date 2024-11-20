<script setup>
//* ===== dependencies =====
import { ref } from 'vue'
import { storeToRefs } from 'pinia';

//* ===== Pinia =====
import { useProjectsStore } from '@/stores/projects'
const { projects } = storeToRefs(useProjectsStore())

//* ===== Shadcn =====
import { Button } from '@/components/ui/button'
import { Icon } from '@iconify/vue'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { Card, CardTitle, CardContent, /*CardDescription,*/ CardFooter, CardHeader }
from '@/components/ui/card'

//* ===== Custom Components =====

import ProjectList from '@/components/ProjectList.vue'

//* ===== Shadcn =====

const devEnvAlert = ref(true)
const setDevEnvAlert = () => {
  console.log("setDevEnvAlert called")
  devEnvAlert.value = !devEnvAlert.value
  localStorage.setItem('devEnvAlert', JSON.stringify(devEnvAlert.value))
}
if (localStorage.getItem('devEnvAlert')) {
  devEnvAlert.value = JSON.parse(localStorage.getItem('devEnvAlert'))
}





const TOFisOpen = ref(false)

console.log(projects)
</script>

<template>
  <main class="relative scroll-smooth scroll-pt-12 flex-1 dark:text-gray-100">
    <section id="temp" v-if="devEnvAlert" class="container mt-2 -mb-4">
      <Alert>
        <Icon icon="mdi:alert-circle-outline" class="w-4 h-4" />
        <AlertTitle>
          Application under development
          <Button class="float-right" variant="outline" size="icon" @click="setDevEnvAlert()">
            <Icon icon="mdi:close" class="w-4 h-4" />
          </Button>
        </AlertTitle>
        <AlertDescription>
          This application is under development and may not work as expected.
        </AlertDescription>
      </Alert>
    </section>
    <section id="presentation" class="mt-16 container flex flex-col justify-center relative">
      <!--
      Madrugada (acessando de madrugada):

      "Howdy, night owl!"
      "Burning the midnight oil?"
      "Up late, are we?"

      Manhã:

      "Good morning, sunshine!"
      "Rise and shine!"
      "Morning, early bird!"

      Tarde:

      "Good afternoon!"
      "Hello, afternoon warrior!"

      Noite:

      "Good evening, night owl!"
      "Winding down?"
      "Evening, sleepyhead!"
      -->
      <h1 class="font-semibold tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white">Alexsander Patrick Ferreira Santos</h1>
      <h2 class="text-2xl mt-1">{{ $t('presentation.subtitle') }}</h2>
      <p class="py-4 mb-4 w-1/2 text-lg font-normal text-gray-500 dark:text-gray-400">
        {{ $t('presentation.description') }}
      </p>
    </section>

    <section id="skills" class="container mt-12">
      <h2 class="text-xl">{{ $t('skills.title') }}</h2>
      <div class="flex flex-wrap gap-4 items-center mt-4 text-gray-700 dark:text-gray-100">
        <article
          class="flex items-center gap-2 py-4 px-8 text-lg rounded-sm border hover:scale-105 transition-transform">
          <Icon icon="mdi:eye-outline" /> {{ $t('skills.list.accessibility') }}
        </article>
        <article
          class="flex items-center gap-2 py-4 px-8 text-lg rounded-sm border hover:scale-105 transition-transform">
          <Icon icon="mdi:shield-check-outline" /> {{ $t('skills.list.security') }}
        </article>
        <article
          class="flex items-center gap-2 py-4 px-8 text-lg rounded-sm border hover:scale-105 transition-transform">
          <Icon icon="mdi:server" /> {{ $t('skills.list.devops') }}
        </article>
      </div>
      <p class="text-base mt-4">{{ $t('skills.description') }}</p>
    </section>

    <ProjectList v-if="projects" id="projects" class="container mt-12" :projects="projects"
      :title="$t('projects.title')" />


    <section id="contacts" class="mt-12 container grid items-center">
      <h2 class="text-xl text-center">{{ $t('contacts.title') }}</h2>
      <section class="flex gap-6 justify-center mb-8 mt-4">
        <Card class="aspect-[5/6] w-[250px] flex flex-col hover:scale-105 transition-transform shadow-sm">
          <CardHeader>
            <CardTitle class="">LinkedIn</CardTitle>
          </CardHeader>
          <CardContent>
            <img
              src="https://media.licdn.com/dms/image/v2/C5603AQEAF-rqzRNM1g/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1640883574386?e=2147483647&v=beta&t=GELyliHb8_HPdiaTcbM1xWhpi04uBigfsD2lk493Ig4"
              class="aspect-square h-14 rounded-full" alt="Alexsander Patrick Ferreira Santos">
            <h4 class="font-semibold">Alexsander Patrick Ferreira Santos</h4>
            <p class="text-sm">Full Stack Developer | DevOps | Web Developer</p>
            <p class="text-xs text-nowrap text-gray-500">Campinas, São Paulo, Brazil</p>
          </CardContent>
          <CardFooter class="flex-1">
            <a href="https://www.linkedin.com/in/alexsander-p-f-santos/" target="_blank" class="ml-auto mt-auto">
              <Button
                variant="outline" class="text-blue-600 dark:text-blue-400">View Profile
              </Button></a>
          </CardFooter>
        </Card>

        <Card class="aspect-[5/6] w-[250px] flex flex-col hover:scale-105 transition-transform shadow-sm">
          <CardHeader>
            <CardTitle class="">GitHub</CardTitle>
          </CardHeader>
          <CardContent>
            <img src="https://avatars.githubusercontent.com/u/82063944?v=4" class="aspect-square h-14 rounded-full"
              alt="Alexsander Patrick Ferreira Santos">
            <h4 class="font-semibold">Sander</h4>
            <p class="text-sm">@Alexsander33set</p>
            <p class="text-xs text-nowrap text-gray-500">Brazil</p>
            <p class="text-xs text-nowrap text-gray-500">{{ new Date().toLocaleString('pt-br', {
              timeZone:
                'America/Sao_Paulo', hour: '2-digit', minute: '2-digit'
            }) }} (UTC -03:00)</p>
          </CardContent>
          <CardFooter class="flex-1">
            <a href="https://github.com/Alexsander33set" target="_blank" class="ml-auto mt-auto"><Button
                variant="outline">View Profile</Button></a>
          </CardFooter>
        </Card>

        <Card class="aspect-[5/6] w-[250px] flex flex-col hover:scale-105 transition-transform shadow-sm">
          <CardHeader>
            <CardTitle class="">Email</CardTitle>
          </CardHeader>
          <CardContent>
            <span class="relative">
              <img src="https://lh3.googleusercontent.com/a/ACg8ocIu8srtWQ-arq38vpMHV-r4-dp32PdBwYdnEStcaGjAURnrsFk=s83-c-mo"
                class="aspect-square h-14 rounded-full" alt="Alexsander Patrick Ferreira Santos">
              <div class="absolute top-0 left-0">
                <svg focusable="false" height="56px" width="56px" version="1.1" viewBox="0 0 40 40" xml:space="preserve"
                  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="opacity:1.0">
                  <path
                    d="M4.02,28.27C2.73,25.8,2,22.98,2,20c0-2.87,0.68-5.59,1.88-8l-1.72-1.04C0.78,13.67,0,16.75,0,20c0,3.31,0.8,6.43,2.23,9.18L4.02,28.27z"
                    fill="#F6AD01"></path>
                  <path
                    d="M32.15,33.27C28.95,36.21,24.68,38,20,38c-6.95,0-12.98-3.95-15.99-9.73l-1.79,0.91C5.55,35.61,12.26,40,20,40c5.2,0,9.93-1.98,13.48-5.23L32.15,33.27z"
                    fill="#249A41"></path>
                  <path
                    d="M33.49,34.77C37.49,31.12,40,25.85,40,20c0-5.86-2.52-11.13-6.54-14.79l-1.37,1.46C35.72,9.97,38,14.72,38,20c0,5.25-2.26,9.98-5.85,13.27L33.49,34.77z"
                    fill="#3174F1"></path>
                  <path
                    d="M20,2c4.65,0,8.89,1.77,12.09,4.67l1.37-1.46C29.91,1.97,25.19,0,20,0l0,0C12.21,0,5.46,4.46,2.16,10.96L3.88,12C6.83,6.08,12.95,2,20,2"
                    fill="#E92D18"></path>
                </svg>
              </div>
            </span>
            <h4 class="font-semibold">Alexsander Patrick</h4>
            <p class="text-sm text-gray-500">alexsander.patrick@gmail.com</p>
          </CardContent>
          <CardFooter class="flex-1">
            <a href="mailto:alexsander.patrick@gmail.com" target="_blank" class="ml-auto mt-auto"><Button
                variant="outline" class="text-jasper-500 dark:text-jasper-500">Send Email</Button></a>
          </CardFooter>
        </Card>
      </section>
    </section>

    <div
      class="absolute top-20 -right-2 hover:-right1 p-2 hover:scale-105 cursor-pointer border rounded-sm text-center duration-300 hover:shadow-md opacity-50 hover:opacity-100 transition-all"
      @click="TOFisOpen = !TOFisOpen" @mouseleave="TOFisOpen = false">
      <Icon icon="mdi:menu-left" class="scale-150 transition-all duration-300" :class="{ 'rotate-180': TOFisOpen }" />
      <Transition  name="fade">
        <div id="tableOfContents" v-if="TOFisOpen" class="flex flex-col gap-2 text-muted-foreground transition-all mt-2">
          <a href="#presentation" class="hover:text-primary hover:underline transition-colors">{{
            $t('tableOfContents.presentation') }}</a>
          <a href="#projects" class="hover:text-primary hover:underline transition-colors">{{
            $t('tableOfContents.projects') }}</a>
          <a href="#contacts" class="hover:text-primary hover:underline transition-colors">{{
            $t('tableOfContents.contacts') }}</a>
        </div>
      </Transition>
    </div>
  </main>
</template>

<style scoped>
/*
#tableOfContents {
  animation: slideIn 0.5s ease-in-out forwards;
}
*/

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  width: 0;
}
/*
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
*/
</style>
