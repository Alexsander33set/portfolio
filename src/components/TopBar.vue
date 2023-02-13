<template>
  <div>
    <div class="navbar">
      <button v-html="showSiteLanguage()" v-on:click="$emit('onLog')"></button>
      <div class="navbarRight">
        <select
          name=""
          id=""
          v-model="this.languageSelected"
          @change="$emit('onLog')"
        >
          <option
            v-for="language in this.supportedLanguages"
            :key="language"
            :value="language.code"
          >
            {{ language.name }}
          </option>
        </select>
        <nav>
          <router-link to="/">Página Inicial</router-link> |
          <router-link to="/about">Sobre</router-link> |
          <router-link to="/WeatherAPI">WeatherAPI</router-link>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "navBar",
  props: {
    preferedLanguage: String,
    supportedLanguages: Array,
  },
  data() {
    return {
      languageSelected: "",
    };
  },
  emits: ["onLog"],
  created() {},
  methods: {
    showSiteLanguage() {
      if (!this.preferedLanguage) {
        return "vazio";
      } else return this.preferedLanguage + ' (v-html)';
    },
  },
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
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

</style>
