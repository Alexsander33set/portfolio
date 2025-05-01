<script setup>
//* ===== dependencies =====
import { ref } from "vue";
import { storeToRefs } from "pinia";

//* ===== Pinia =====
import { useProjectsStore } from "@/stores/projects";
const { projects, isFetchingProjects } = storeToRefs(useProjectsStore());

//* ===== Shadcn =====

//* ===== Custom Components =====

</script>

<template>
  <main class="relative scroll-smooth scroll-pt-12 flex-1 dark:text-gray-100">
    <section class="container mt-2">
      About page
    </section>
  </main>
</template>

<style scoped>

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  width: 0;
}

@keyframes appear-to-top {
  from {
    transform: translateY(100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}
#presentation > *, #end-main {
  opacity: 0;
  animation: appear-to-top 800ms ease-out forwards;
}
#presentation-greetings {
  animation-delay: 300ms;
  @apply text-3xl;
}

#presentation-self {
  animation-delay: 1s;
}
#presentation-self-description {
  animation-delay: 1.3s;
}

#end-main {
  animation-delay: 1.7s;
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
