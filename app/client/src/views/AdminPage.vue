<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
//* ===== Shadcn =====
import { Icon } from '@iconify/vue'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'


const token = localStorage.getItem('token')

if (!token) {
  setTimeout(() => {
    router.push('/login')
  }, 2000)
}
</script>

<template>
  <main class="container">  
    <template v-if="!token">
      <Alert variant="destructive">
        <Icon icon="lucide:alert-circle" class="w-4 h-4" />
        <AlertTitle>Error</AlertTitle>
        <AlertDescription>
          Your session has expired. Please log in again.
        </AlertDescription>
      </Alert>
    </template>
    
    <template v-else>
      <h1>Admin Page</h1>
    </template>
  </main>
</template>