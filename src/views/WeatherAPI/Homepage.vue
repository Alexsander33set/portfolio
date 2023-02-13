<template>
  <!-- <div>
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
          <div>{{ (this.bruteWeatherData.main.temp-273.15).toFixed(2)}} º C | º F |  º C</div>
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
  </div>
    <template v-else>Ops! alguem erro ocorreu...</template> -->

  <div class="mainBody">
    <div class="navbar">Navbar</div>
    <main class="mainContainer">
      <div>Atualizado em 0m</div>
      <div class="weatherIcon"><img :src="'http://openweathermap.org/img/wn/'+this.bruteWeatherData.weather[0].icon+'@2x.png'" :alt="this.bruteWeatherData.weather[0].description" ></div>
      <div class="weatherCity">{{ this.bruteWeatherData.name }}</div>
      <div class="mainTemperature">
        <div class="averageTemp">{{ (this.bruteWeatherData.main.temp-273.15).toFixed(2)}} º C</div>
        <div class="maxMinTemp">
          <div class="maxTemp"><i></i><p>↑{{(this.bruteWeatherData.main.temp_max-273.15).toFixed(2)}} ºC</p></div>
          <div class="maxTemp"><i></i><p>↓{{(this.bruteWeatherData.main.temp_min-273.15).toFixed(2)}} ºC</p></div>
        </div>
      </div>
      <div class="tempTex">{{ this.bruteWeatherData.weather[0].description }}</div>
      <div class="cardsContainer">
        <article class="card grid2">
          <h6>Sensaçào Térmica</h6>
          <p>{{ this.bruteWeatherData.main.feels_like }}</p>
        </article>
        <article class="card">
          <h6>Visibilidade</h6>
          <p>{{ this.bruteWeatherData.visibility/100 }} %</p>
        </article>
        <article class="card">
          <h6>Humidade</h6>
          <p>{{ this.bruteWeatherData.main.humidity }} %</p>
        </article>
        <article class="card">
          <h6>Vento</h6>
          <p>{{ this.bruteWeatherData.wind.speed }} m/s</p>
        </article>
      </div>
    </main>
    <footer>Footer</footer>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "WeatherHome",
  data() {
    return {
      userWeatherPreferences: { metricUnit: "" },
      bruteWeatherData: {
        coord: {
          lon: 10.99,
          lat: 44.34,
        },
        weather: [
          {
            id: 501,
            main: "Rain",
            description: "moderate rain",
            icon: "10d",
          },
        ],
        base: "stations",
        main: {
          temp: 298.48,
          feels_like: 298.74,
          temp_min: 297.56,
          temp_max: 300.05,
          pressure: 1015,
          humidity: 64,
          sea_level: 1015,
          grnd_level: 933,
        },
        visibility: 10000,
        wind: {
          speed: 0.62,
          deg: 349,
          gust: 1.18,
        },
        rain: {
          "1h": 3.16,
        },
        clouds: {
          all: 100,
        },
        dt: 1661870592,
        sys: {
          type: 2,
          id: 2075663,
          country: "IT",
          sunrise: 1661834187,
          sunset: 1661882248,
        },
        timezone: 7200,
        id: 3163858,
        name: "Zocca",
        cod: 200,
      },
      userInputs: { city: "", stateCode: "", countryCode: "" },
      limit: 1,
      lat: "",
      lon: "",
      geoCity: "",
      geocityLocation: "",
    };
  },
  created() {
    this.getGeolocatization();
  },
  methods: {
    getGeolocatization() {
      let successCallback = (position) => {
        console.log(position);
        this.lat = position.coords.latitude.toFixed(2);
        this.lon = position.coords.longitude.toFixed(2);
      };
      let errorCallback = (error) => {
        console.log(error);
      };
      navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    },
    getWeather() {
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
          this.bruteWeatherData = response.data;
          console.log(this.bruteWeatherData);
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
          this.geocityLocation =
            response.data.name + ", " + response.data.state;
        });
    },
    temperatureConverting(converting, temperature = Number) {
      converting;
      if (!temperature) {
        return;
      }
      converting == "kelvin2ceusius" ? temperature - 272 : "";
    },
  },
};
</script>

<style >
.mainBody {background: #E5ECF4}
.navbar {
  height: 56px;
  background: rgba(0, 128, 0, 0.13);
}
.cardsContainer{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(96px, 1fr));
  margin: 12px;
  background: rgba(255, 255, 0, 0.425);
  gap: 12px;
}
.card{background: white;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
  height: 96px;
  padding: 8px;
}
.card h6{
  font-weight: 400;
  font-size: 14;
  color: #363636;
}
.card p{
  font-weight: 500;
  font-size: 20;
  color: #444444;
}
.grid2{grid-column: 1/3;}

@media (min-width: 1024px) {
  .weatherContainer {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  }
  .weatherCard {
    background: rgba(100, 200, 255, 0.2);
    box-shadow: 2px 2px 8px -1px black;
    border-radius: 16px;
    margin: 24px 8px;
    padding: 1rem 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 24px;
    font-size: 2.7rem;
    max-width: max-content;
  }
  .weatherCard img {
    height: 120%;
  }
  .weatherCard .tempData .minMax {
    font-size: 0.725rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
  }
}
</style>
