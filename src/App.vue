<template>
  <!--<div style="height: 100px; width: 100px; background: red" @click="any()"/>-->
  
  <router-view />
</template>

<script>

export default {
  data() {
    return {
      preferedLanguage: "",
      darkTheme: "",
      supportedLanguages: [
        { name: "Português Brasil", code: "pt-BR" },
        { name: "English", code: "en-US" },
      ],
    };
  },
  created() {
    this.checkLanguages();
    this.getTheme();
  },
  methods: {
    checkLanguages() {
      //SE NÃO TIVER O USER LANGUAGE NO LOCAL STORAGE, DEFINE POR PADRÃO DO BROWSER
      if (!localStorage.getItem("userLanguage")) {
        localStorage.setItem("userLanguage", navigator.language);
      }
      this.preferedLanguage = localStorage.getItem("userLanguage");
      /*|||||*/ console.log(
        " Preferência de linguagem usuário - LocalStorage: " +
          this.preferedLanguage
      );
    },
    getTheme(){
      window
      .matchMedia("(prefers-color-scheme: dark)")
      .addEventListener("change", (event) => {
        this.darkTheme = event.matches ? "dark" : "light";
      });
    },
    onLogi() {
      console.log("logado do filho");
    },
    any() {
      this.darkTheme=window.matchMedia("(prefers-color-scheme: dark)").matches;
      console.log(this.darkTheme ? "dark" : "light");
    },
  },
};
</script>
<style lang="scss"> 
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html,body,.mainBody{min-width: 100dvw; min-height: 100dvh;}

#app {
  font-family:Inter, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  min-height: 100dvh;
}
/*
@media (prefers-color-scheme: dark)
{
  #app {
    background: #000f1d;
    color: white;
  }
  nav{
    a{color:#6f85d2;}
  }
}
@media (prefers-color-scheme: light)
{
  #app {
    background: #E3E3E3;
    color: #121212;
  }
  nav {
  a {
    color:#2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
}
nav {
  padding: 30px;

  a {
    font-weight: bold;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
button {
  padding: 0.5rem;
  text-transform: capitalize;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-weight: 600;
  box-shadow: inset 0 0 2px 0px #42b983;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;

  &:hover {
    background: #42b983;
    outline: 2px solid #c6c6c6;
    outline-offset: 2px;
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
---------------------------------*/
</style>
