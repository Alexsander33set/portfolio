<script setup>
import { RouterView } from 'vue-router'
import Navbar from './components/layout/Navbar.vue'
import FooterComponent from './components/layout/FooterComponent.vue'
</script>

<template>
  <Navbar />
  <RouterView />
  from App.vue: {{ $t('hello') }}
  <FooterComponent />
</template>
