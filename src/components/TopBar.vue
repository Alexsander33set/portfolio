<template>
  <div class="TopBar">
    <button @click="changePageLanguage">mudar linguagem padrão pra portugues brasileiro</button>
    <nav >
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
  </div>

</template>

<script>
export default {
  name: 'TopBar',
  props: {
    msg: String
  },
  methods:{
    changePageLanguage(){
      localStorage.setItem('userLanguage', 'pt-BR')
  },
 
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">


.TopBar{
  background: rgba(163, 250, 151, 0.247);
  display: flex;
  align-items: center;
  justify-content: space-around;
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
</style>
