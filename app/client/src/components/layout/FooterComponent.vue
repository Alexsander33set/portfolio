<script setup>
import { RouterLink } from 'vue-router'

import { usePreferencesStore } from '@/stores/preferences'
const language = usePreferencesStore().language

</script>

<template>
  <footer class="bg-zinc-900 text-white py-8">
    <div class="container mx-auto px-4">
      <div class="flex flex-col md:flex-row justify-between items-center">
        <div class="mb-4 md:mb-0">
          <p class="text-sm">{{ $t('footer.copyright') }}</p>
        </div>
        <div class="flex space-x-4">
          <RouterLink :to="`/${language}/privacy-&-acceptance-terms`" class="hover:text-zinc-300 transition-colors duration-300">{{ $t('footer.privacy') }}</RouterLink>
          <a href="#contacts" class="hover:text-zinc-300 transition-colors duration-300">{{ $t('footer.contacts') }}</a>
        </div>
      </div>
    </div>
  </footer>
</template>
