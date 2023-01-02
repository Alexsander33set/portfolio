<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <TopBar msg="TopBar"/>
  </div>
</template>

<script>
// @ is an alias to /src
import TopBar from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    TopBar
  }
}
</script>
