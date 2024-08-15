<script setup>
import { RouterView } from 'vue-router'
import Navbar from './components/layout/Navbar.vue'
import FooterComponent from './components/layout/FooterComponent.vue'
</script>

<template>
  <Navbar />
  from App.vue: {{ $t('hello') }}
  <router-view v-slot="{ Component }">
    <Transition>
      <component :is="Component" />
    </Transition>
  </router-view>
  <FooterComponent />
</template>

<style>
.v-enter-active,
.v-leave-active {
  transition: opacity 500ms ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
