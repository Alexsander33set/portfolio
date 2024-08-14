<script setup>
import { RouterView } from 'vue-router'
import Navbar from './components/layout/Navbar.vue'
import FooterComponent from './components/layout/FooterComponent.vue'
</script>

<template>
  <Navbar />
  from App.vue: {{ $t('hello') }}
  <Transition name="fade">
    <RouterView />
  </Transition>
  <FooterComponent />
</template>

<style>

.fade-enter-from,
.fade-leave-from{
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active{
  transition: opacity 500ms;
}

.fade-enter-to,
.fade-leave-to{
  opacity: 1;
}

</style>
