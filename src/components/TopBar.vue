<template> 
<div>
  <div class="navbar">
    <button v-html="showSiteLanguage()"></button>
    <div class="navbarRight">
      <select name="" id="" v-model="this.PreferedLanguage">
        <option 
          v-for="language in this.supportedLanguages" 
          :key="language" :value="language.code">
            {{language.name}}
        </option>
      </select>
      <nav>
        <router-link to="/">Página Inicial</router-link> |
        <router-link to="/about">Sobre</router-link>
      </nav>
    </div>
    
  </div>
  
  
  
  
  
  
  
  
  
  Topbar Component
  <button 
  v-html="showSiteLanguage()"
    v-on:click="$emit('onLog')"></button>
</div>


</template>

<script>
export default {
  name: 'TopBar',
  props:{
    preferedLanguage: String,
    supportedLanguages: Array,
  },
  data(){
    return{
      languageSelected:''
    }
  },
  emits:['onLog'],
  created(){},
  methods: {
    showSiteLanguage(){
    if (!this.preferedLanguage){
      return 'vazio'
    }
    else return this.preferedLanguage
    },
  },
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">



</style>
