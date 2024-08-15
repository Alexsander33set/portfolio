<script setup>
import { RouterLink } from 'vue-router'

import { usePreferencesStore } from '@/stores/preferences'
const prefStore = usePreferencesStore()

import { useColorMode } from '@vueuse/core'
const mode = useColorMode()

import { Icon } from '@iconify/vue'
import { Button } from '@/components/ui/button'
import { Separator } from '@/components/ui/separator'
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger
}from '@/components/ui/dropdown-menu'
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'


</script>

<template>
  <header class="flex justify-between p-2 shadow-md bg-zinc-950 text-white">
    <div class="logo">
      <img src="@/assets/logo-white.svg" alt="APFS logo in letters">
      {{ prefStore }}
    </div>
    <nav class="inline-flex gap-2 items-center p-1">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <Separator orientation="vertical" />
      <Select id="language-changer">
        <SelectTrigger>
          <SelectValue placeholder="Select a fruit" />
        </SelectTrigger>
        <SelectContent>
            <SelectItem v-for="(language, index) in prefStore.acceptedLanguages" :key="index" :value="language.value" @click="prefStore.toggleLanguage($i18n, language.value)"> 
              {{language.label}}
            </SelectItem>
        </SelectContent>
      </Select>
      
      <!-- <v-menu  transition="scale-transition" v-bind="props">
        <template v-slot:activator="{ props }">
          <v-btn icon="mdi-translate" v-bind="props" color="primary"></v-btn>
        </template>
        <v-list>
          <v-list-item v-for="(language, index) in preferences.acceptedLanguages" :key="index" :value="language.value" @click="preferences.toggleLanguage($i18n, language.value)">
            <v-list-item-title>{{language.label}}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu> -->
      <DropdownMenu>
        <DropdownMenuTrigger as-child>
          <Button variant="outline">
            <Icon icon="radix-icons:moon" class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
            <Icon icon="radix-icons:sun" class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
            <span class="sr-only">Toggle theme</span>
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent align="end">
          <DropdownMenuItem @click="mode = 'light'">
            Light
          </DropdownMenuItem>
          <DropdownMenuItem @click="mode = 'dark'">
            Dark
          </DropdownMenuItem>
          <DropdownMenuItem @click="mode = 'auto'">
            System
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </nav>
  </header>
</template>


<style scoped>



</style>