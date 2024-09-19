


<script setup>
import { ref } from 'vue'

import { useRouter } from 'vue-router'
const router = useRouter()

import axios from 'axios'
//* shadcn
//* ===== Shadcn =====
import { Icon } from '@iconify/vue'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import Button from '@/components/ui/button/Button.vue';

//* ====================== Attempts ======================
const maxLoginAttempts = 5
const maxLoginAttemptsReached = ref(false)

class LoginAttempts {
  constructor(attempts = 0, firstAttempt = null) {
    if (localStorage.getItem('attempts')) {
      const {attempts, firstAttempt} = JSON.parse(localStorage.getItem('attempts'))
      this.attempts = attempts
      this.firstAttempt = firstAttempt
      return
    }  
    this.attempts = attempts
    this.firstAttempt = firstAttempt
  }
  save() {
    localStorage.setItem('attempts', JSON.stringify(this))
  }
  clear() {
    localStorage.removeItem('attempts')
  }
  cleanAttemptsAfterTime(time){
    /* time is in milliseconds */
    if (!this.firstAttempt) return

    const currentTime = new Date()
    const timeDifference = currentTime.getTime() - this.firstAttempt.getTime()
    if (timeDifference > time) {
      this.clear()
    }
  }
  checkMaxAttemptsReached(maxLoginAttempts) {
    return this.attempts >= maxLoginAttempts
  }
  addAttempt() {
    this.attempts++
    if (this.firstAttempt === null) {
      this.firstAttempt = new Date()
    }
    this.save()
  }
}


const attempts = new LoginAttempts()
attempts.cleanAttemptsAfterTime(1000 * 60 * 60)
maxLoginAttemptsReached.value = attempts.checkMaxAttemptsReached(maxLoginAttempts)


//* ====================== Login ======================
const email = ref('')
const password = ref('')

const login = function() {
  if (attempts.checkMaxAttemptsReached(maxLoginAttempts)) {
    maxLoginAttemptsReached.value = true
    /* TODO: add notification component */
    return
  }

  axios.post('/auth/login', {
    email: email.value,
    password: password.value
  })
  .then((res)=>{
    console.log(res)
    
    if (!res.data.success) {
      /* TODO: add notification component */
      console.log(res)
      alert('Invalid credentials')
      attempts.addAttempt()
      return
    }

    let {token} = res.data
    localStorage.setItem('token', token)
    attempts.clear()
    router.push('/admin')
  })
  .catch((err)=>{
    console.log(err)
    /* TODO: add notification component */
    alert('Something went wrong! Check the endpoint.')
    attempts.addAttempt()
  })
}
</script>

<template>
  <main class="container flex flex-col items-center justify-center h-screen bg-slate-700 dark:bg-slate-900 transition-colors">
    <template v-if="maxLoginAttemptsReached.value">
      <Alert variant="destructive">
        <Icon icon="lucide:alert-circle" class="w-4 h-4" />
        <AlertTitle>Error</AlertTitle>
        <AlertDescription>
          Too many attempts, try again later
        </AlertDescription>
      </Alert>
    </template>

    <form @submit.prevent="login" class="flex flex-col gap-4 p-8 border rounded-md shadow-sm bg-white dark:text-black">
      <h1 class="text-2xl font-bold">Login</h1>
      <div class="grid items-center gap-1.5">
        <Label for="email">Email</Label>
        <Input id="email" type="email" v-model="email" placeholder="Email" />
      </div>

      <div class="grid items-center gap-1.5">
        <Label for="password">Password</Label>
        <Input id="password" type="password" v-model="password" placeholder="Password" />
      </div>
      <div class="grid">
        <Button type="submit" variant="outline" class="dark:text-white">Login</Button>
      </div>
    </form>
  </main>
</template>