<template>
  <div>
    something
    <input type="text" placeholder="Nome da Cidade" v-model="userInputs.city" />
    <input
      type="text"
      placeholder="Código do estado"
      v-model="userInputs.stateCode"
    />
    <input
      type="text"
      placeholder="Código do país"
      v-model="userInputs.countryCode"
    />
    <input type="text" placeholder="Limite" v-model="limit" required="true" />
    <button @click="getCoordinates()">try get API</button>
    <div><button @click="getWeather()">try get API Weather</button></div>
    <br /><hr /><br />
    <button @click="getCity()">Location</button>
    <input type="text" disabled="true" v-model="geocityLocation"/>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "WeatherHome",
  data() {
    return {
      apiKey: process.env.VUE_APP_API_KEY,
      userInputs: { city: "", stateCode: "", countryCode: "" },
      limit: "",
      lat: "",
      lon: "",
      geoCity: "",
      geocityLocation:'',
    };
  },
  created() {
    this.getGeolocatization();
  },
  methods: {
    getGeolocatization() {
      const successCallback = (position) => {
        console.log(position);
        this.lat = position.coords.latitude.toFixed(2);
        this.lon = position.coords.longitude.toFixed(2);
      };
      const errorCallback = (error) => {
        console.log(error);
      };

      navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    },
    getCoordinates() {
      //https://openweathermap.org/api/geocoding-api
      const apiCallByCity =
        "http://api.openweathermap.org/geo/1.0/direct?q=" +
        this.userInputs.city +
        "&limit=" +
        this.limit +
        "&appid=";
      const apiCallByStateCode =
        "http://api.openweathermap.org/geo/1.0/direct?q=" +
        this.userInputs.stateCode +
        "&limit=" +
        this.limit +
        "&appid=";
      const apiCallByCountryCode =
        "http://api.openweathermap.org/geo/1.0/direct?q=" +
        this.userInputs.countryCode +
        "&limit=" +
        this.limit +
        "&appid=";
      console.log(
        "ByStateCode: " +
          apiCallByStateCode +
          "\nByCountryCode: " +
          apiCallByCountryCode +
          "\nByCityName: " +
          apiCallByCity
      );
      axios
        .get(apiCallByCountryCode + process.env.VUE_APP_API_KEY)
        .then((response) => {
          console.log(response.data);
        });
    },
    getWeather() {
      // https://openweathermap.org/current
      axios
        .get(
          "https://api.openweathermap.org/data/2.5/weather?lat=" +
            this.lat +
            "&lon=" +
            this.lon +
            "&appid=" +
            process.env.VUE_APP_API_KEY
        )
        .then((response) => {
          console.log(response.data);
        });
    },
    getCity() {
      axios
        .get(
          "http://api.openweathermap.org/geo/1.0/reverse?lat=" +
            this.lat +
            "&lon=" +
            this.lon +
            "&limit=1&appid=" +
            process.env.VUE_APP_API_KEY
        )
        .then((response) => {
          console.log(response.data);
          this.geoCity = response.data;
          this.geocityLocation = response.data[0].name +', ' + response.data[0].state
        });
    },
  },
};
</script>
