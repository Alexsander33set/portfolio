<template>
  <topBar 
    :preferedLanguage="this.preferedLanguage"
    :supportedLanguages="this.supportedLanguages"
    @onLog="onLogi"
  />
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>
// @ is an alias to /src
import topBar from "./../components/TopBar.vue";
export default {
  name: 'HomeView',
  components: {
    topBar,
  },
}

</script>

<style>

</style>