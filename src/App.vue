<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <button @click="changePageLanguage">mudar linguagem padrão pra portugues brasileiro</button>
  <router-view/>
</template>

<script>
export default {
data(){return{userPreferedLanguage:'',}},
created() {
    this.checkLanguages()
   
},
methods:{
  checkLanguages(){
    //SE NÃO TIVER O USER LANGUAGE NO LOCAL STORAGE, DEFINE POR PADRÃO DO BROWSER
    if(!localStorage.getItem('userLanguage')){
      localStorage.setItem('userLanguage', navigator.language)
    }
    this.userPreferedLanguage = localStorage.getItem('userLanguage')

    console.log(' Preferência de linguagem usuário - LocalStorage: '+this.userPreferedLanguage)
  },
  changePageLanguage(){
    localStorage.setItem('userLanguage', 'pt-BR')
  }
}
}
</script>
<style lang="scss">
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
</style>
