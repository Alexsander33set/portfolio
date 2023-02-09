<template>
  <div class="mainBody">
    <input type="text" placeholder="Nome da Cidade" v-model="userInputs.city" />
    <input type="text" placeholder="Código do estado" v-model="userInputs.stateCode" />
    <input type="text" placeholder="Código do país" v-model="userInputs.countryCode" />
    <input type="text" placeholder="Limite" v-model="limit" required="true" />
    <button @click="getCoordinates()">try get API</button>
    <div><button @click="getWeather()">try get API Weather</button></div>
    <br />
    <hr /><br />
    <button @click="getCity()">Location</button>
    <input type="text" disabled="true" v-model="geocityLocation" />
    <br>
    <hr /><br>
    <div class="weatherInfo">
      <h1>getAPIData</h1><br>

      <h5>Location: <p>{{ this.bruteWeatherData.name }} - Longitude: {{ this.lon ? this.lon : "Sem acesso" }} | Latitude:
          {{ this.lat ? this.lat : "Sem acesso" }}</p>
      </h5>
      <div class="containerTemp">
        <img src="http://openweathermap.org/img/wn/10d@2x.png" alt=""/>
        <div class="tempData">
          <div>{{ (this.bruteWeatherData.main.temp-273.15).toFixed(2)}}<!-- º C | º F | --> º C</div>
          <div class="minMax"><p>{{"Min: "+ (this.bruteWeatherData.main.temp_min-273.15).toFixed(2)}} º</p><p>Max: {{ (this.bruteWeatherData.main.temp_max-273.15).toFixed(2) }} º</p></div>
        </div>
      </div>     
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "WeatherHome",
  data() {
    return {
      userWeatherPreferences: { metricUnit: '', },
      bruteWeatherData:
      {
        "coord": {
          "lon": -0.13,
          "lat": 51.51
        },

        "weather": [

          {
            "id": 300,
            "main": "Drizzle",
            "description": "light intensity drizzle",
            "icon": "09d"
          }
        ],
        "base": "stations",

        "main": {
          "temp": 280.32,
          "pressure": 1012,
          "humidity": 81,
          "temp_min": 279.15,
          "temp_max": 281.15
        },
        "visibility": 10000,

        "wind": {
          "speed": 4.1,
          "deg": 80
        },

        "clouds": {
          "all": 90
        },
        "dt": 1485789600,

        "sys": {
          "type": 1,
          "id": 5091,
          "message": 0.0103,
          "country": "GB",
          "sunrise": 1485762037,
          "sunset": 1485794875
        },
        "id": 2643743,
        "name": "London",
        "cod": 200
      },
      userInputs: { city: "", stateCode: "", countryCode: "" },
      limit: "",
      lat: "", lon: "",
      geoCity: "",
      geocityLocation: '',
    };
  },
  created() {
    this.getGeolocatization();
  },
  methods: {
    showUserPreference() { console.log(this.preferedLanguage) },
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
        "http://api.openweathermap.org/geo/1.0/direct?q=" + this.userInputs.city + "&limit=" + this.limit + "&appid=";
      const apiCallByStateCode =
        "http://api.openweathermap.org/geo/1.0/direct?q=" +
        this.userInputs.stateCode + "&limit=" + this.limit + "&appid=";
      const apiCallByCountryCode =
        "http://api.openweathermap.org/geo/1.0/direct?q=" +
        this.userInputs.countryCode + "&limit=" + this.limit + "&appid=";
      console.log(
        "ByStateCode:" + apiCallByStateCode + "\nByCountryCode: " + apiCallByCountryCode + "\nByCityName: " + apiCallByCity
      );
      axios
        .get(apiCallByCountryCode + process.env.VUE_APP_API_KEY)
        .then((response) => {
          console.log(response.data);
        });
    },
    getWeather() {
      axios
        .get(
          "https://api.openweathermap.org/data/2.5/weather?lat="
          + this.lat + "&lon=" + this.lon + "&appid=" + process.env.VUE_APP_API_KEY)
        .then((response) => {
          console.log(response.data);
          this.bruteWeatherData = response.data;
          console.log(this.bruteWeatherData)
        });
    },
    getCity() {
      axios
        .get("http://api.openweathermap.org/geo/1.0/reverse?lat=" +
          this.lat + "&lon=" + this.lon + "&limit=1&appid=" + process.env.VUE_APP_API_KEY
        )
        .then((response) => {
          console.log(response.data);
          this.geoCity = response.data;
          this.geocityLocation = response.data[0].name + ', ' + response.data[0].state
        });
    },
  },
};
</script>

<style>
.containerTemp{
  background: rgba(100,200,255,0.2);
  box-shadow: 2px 2px 8px -1px black;
  border-radius:16px;
  margin: 24px 8px;
  padding: 1rem 2rem;
  display:flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  font-size: 2.7rem;
  max-width:max-content;
}
.containerTemp img{
      height: 120%;
    }
    .containerTemp .tempData .minMax{
      font-size: .725rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
    }
</style>