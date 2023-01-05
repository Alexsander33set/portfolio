<template>
  <div class="navbar">
    <button v-html="showSiteLanguage()"></button>
    <button @click="changeLanguage('en-US')">mudar linguagem padrão pra Inglês</button>
    <div class="navbarRight">
      <select name="" id="">
        <option v-for="language in this.supportedLanguages" :key="language">{{language}}</option>
      </select>
      <nav>
        <router-link to="/">Página Inicial</router-link> |
        <router-link to="/about">Sobre</router-link>
      </nav>
    </div>
    
  </div>
  <topBar @changeLanguage="changeLanguage"/>
  <router-view/>
</template>

<script>
import topBar from "./components/TopBar.vue";
export default {
data(){
  return{
    userPreferedLanguage:'',
    supportedLanguages:['pt-BR','en-US'],
  }},
created() {
    this.checkLanguages()
},
components: {
  topBar
},
methods:{
  checkLanguages(){
    //SE NÃO TIVER O USER LANGUAGE NO LOCAL STORAGE, DEFINE POR PADRÃO DO BROWSER
    if(!localStorage.getItem('userLanguage')){
      localStorage.setItem('userLanguage', navigator.language)
    }
    this.userPreferedLanguage = localStorage.getItem('userLanguage')
    /*|||||||||||||||||||*/console.log(' Preferência de linguagem usuário - LocalStorage: '+this.userPreferedLanguage)
  },
  showSiteLanguage(){
    if (!this.userPreferedLanguage){
      return 'vazio'
    }
    else return this.userPreferedLanguage
  },
  changeLanguage(selectedLanguage){
      this.userPreferedLanguage = selectedLanguage
      localStorage.setItem('userLanguage', selectedLanguage)
      //Mudou linguagem no localStorage e setou o language global para pegar de lá
  },
},
}
</script>
<style lang="scss">
*{margin:0;padding:0;box-sizing:border-box;}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
button{
  padding:.5rem;
  text-transform:capitalize;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-weight: 600;
  box-shadow: inset 0 0 2px 0px #42b983;
  border: none;
  border-radius: .5rem;
  cursor: pointer;

  &:hover{
    background: #42b983;
    outline: 2px solid #c6c6c6;
    outline-offset: 2px;
  }
}

/*---------------------------------*/
.navbar{
  background: rgba(163, 250, 151, 0.247);
  display: flex;
  align-items: center;
  justify-content: space-around;

  .navbarRight{
    display:flex;
    align-items: center;
  }
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
/*---------------------------------*/



</style>
