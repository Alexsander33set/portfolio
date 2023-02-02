<template >
  <topBar 
    :preferedLanguage="this.preferedLanguage"
    :supportedLanguages="this.supportedLanguages"
    @onLog="onLogi"
  />
  <div
    style="height: 100px; width: 100px; background: red"
    @click="any()"
  ></div>
  
  <router-view />
</template>

<script>
import topBar from "./components/TopBar.vue";
export default {
  data() {
    return {
      preferedLanguage: "",
      preferedTheme: "",
      supportedLanguages: [
        { name: "Português Brasil", code: "pt-BR" },
        { name: "English", code: "en-US" },
      ],
    };
  },
  created() {
    this.checkLanguages();
    window
      .matchMedia("(prefers-color-scheme: dark)")
      .addEventListener("change", (event) => {
        this.preferedTheme = event.matches ? "dark" : "light";
      });
  },
  components: {
    topBar,
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
    onLogi() {
      console.log("logado do filho");
    },
    any() {
      this.preferedTheme =
        window.matchMedia &&
        window.matchMedia("(prefers-color-scheme: dark)").matches;
      console.log(this.preferedTheme ? "dark" : "light");
    },
  },
};
</script>
<style lang="scss">
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav.dark{
  background: #121212;
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

/*---------------------------------*/
.navbar {
  background: rgba(255, 255, 255, 0.08);
  border-bottom: 1px solid #fff ;
  display: flex;
  align-items: center;
  justify-content: space-around;

  .navbarRight {
    display: flex;
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
