<script setup>
import { RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue'
import FooterComponent from './components/FooterComponent.vue'
</script>

<template>
  <Navbar />
  <RouterView />
  <FooterComponent />
</template>
