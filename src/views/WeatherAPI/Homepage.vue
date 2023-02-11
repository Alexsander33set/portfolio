<template>
  <div class="mainBody">
    <button @click="getCoordinates()">try get API</button><br><br>
    <button @click="getWeather()">try get API Weather</button>
    <br><br>
    <hr /><br />
    <button @click="getCity()">Location</button>
    <input type="text" disabled="true" v-model="geocityLocation" />
    <br>
    <hr /><br>
    <div class="weatherInfo" v-if="this.bruteWeatherData.cod==200">
      <h1>getAPIData</h1><br>

      <h5>Location: <p>{{ this.bruteWeatherData.name }} - Longitude: {{ this.lon ? this.lon : "Sem acesso" }} | Latitude:
          {{ this.lat ? this.lat : "Sem acesso" }}</p>
      </h5>
      <div class="weatherContainer">
        <article class="weatherCard">
        <img src="http://openweathermap.org/img/wn/10d@2x.png" alt=""/>
        <div class="tempData">
          <div>{{ (this.bruteWeatherData.main.temp-273.15).toFixed(2)}}<!-- º C | º F | --> º C</div>
          <div class="minMax"><p>{{"Min: "+ (this.bruteWeatherData.main.temp_min-273.15).toFixed(2)}} º</p><p>Max: {{ (this.bruteWeatherData.main.temp_max-273.15).toFixed(2) }} º</p></div>
        </div>
        <div class="selectMetricUnit" style="gap:12px;">
            <div style="font-size:1rem; user-select: none; cursor:pointer;" @click="this.userWeatherPreferences.metricUnit='C'">°C</div>
            <div style="font-size:1rem; user-select: none; cursor:pointer;" @click="this.userWeatherPreferences.metricUnit='F'">°F</div>
            <div style="font-size:1rem; user-select: none; cursor:pointer;" @click="this.userWeatherPreferences.metricUnit='K'"> °K</div>
        </div>
      </article>     
      <article class="weatherCard">
        <div class="tempData" style="font-size:1rem;">
          <div>Pressão: {{ this.bruteWeatherData.main.pressure}} mb</div>
        </div>
      </article> 
      <article class="weatherCard">
        <div class="tempData" style="font-size:1rem;">
          <div>Humidade: {{ this.bruteWeatherData.main.humidity}}%</div>
        </div>
      </article>
      <article class="weatherCard">
        <div class="tempData" style="font-size:1rem;">
          <div>Visibilidade: {{ (this.bruteWeatherData.visibility/100) + "%"}}</div>
        </div>
      </article>
      <article class="weatherCard">
        <div class="tempData" style="font-size:1rem;">
          <div>Velocidade do vento: {{ this.bruteWeatherData.wind.speed + "m/h"}}</div>
        </div>
      </article>
      </div>    
    </div>
    <template v-else>Ops! alguem erro ocorreu...</template>
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
      limit: 1,
      lat: "", lon: "",
      geoCity: "",
      geocityLocation: '',
    };
  },
  created() {
    this.getGeolocatization();
  },
  methods: {
    getGeolocatization() {
      let successCallback = (position) => {
        console.log(position);
        this.lon = position.coords.latitude.toFixed(2);
        this.lat = position.coords.longitude.toFixed(2);
      };
      let errorCallback = (error) => {
        console.log(error);
      };
      navigator.geolocation.getCurrentPosition(successCallback, errorCallback);

      
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
          this.geocityLocation = response.data.name + ', ' + response.data.state
        });
    },
    temperatureConverting(converting, temperature=Number){
      converting
      if (!temperature) {return}
      converting=='kelvin2ceusius' ? temperature-272 : '';
    },
  },
};
</script>

<style>

.weatherContainer{
  display: grid;
  grid-template-columns: repeat( auto-fit, minmax(400px, 1fr));
}
.weatherCard{
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
.weatherCard img{
      height: 120%;
    }
    .weatherCard .tempData .minMax{
      font-size: .725rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
    }
</style>