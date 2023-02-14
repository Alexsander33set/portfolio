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
      </h5>-->

  <div class="mainBody">
    <div class="navbar">Navbar</div>
    <main class="mainContainer" v-if="true">
      <div class="updatedIn">Atualizado em 0m <img src="../../assets/icons/update.svg" height="12"/></div>
      <div class="weatherIcon"><img :src="'http://openweathermap.org/img/wn/'+this.bruteWeatherData.weather[0].icon+'@2x.png'" :alt="this.bruteWeatherData.weather[0].description" ></div>
      <div class="weatherCity">{{ this.bruteWeatherData.name + ", " + this.bruteWeatherData.sys.country }} <img @click="getWeather()" src="../../assets/icons/edit.svg"/></div>
      <div class="mainTemperature">
        <div class="averageTemp">{{ (this.bruteWeatherData.main.temp-273.15).toFixed(0)}} ºC</div>
        <div class="maxMinTemp">
          <div class="maxTemp"><i>↑</i><p>{{(this.bruteWeatherData.main.temp_max-273.15).toFixed(2)}} ºC</p></div>
          <div class="minTemp"><i>↓</i><p>{{(this.bruteWeatherData.main.temp_min-273.15).toFixed(2)}} ºC</p></div>
        </div>
      </div>
      <div class="tempTex">{{ this.bruteWeatherData.weather[0].description }}</div>
      <div class="cardsContainer">
        <article class="card grid2">
          <h6>Sensaçào Térmica</h6>
          <p>{{ (this.bruteWeatherData.main.feels_like-273.15).toFixed(2) }} ºC</p>
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
    <main v-else>Ops! alguem deu errado...</main>
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
      timestamp:'',
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
        this.timestamp= new Date(position.timestamp); 
      };
      let errorCallback = (error) => {
        console.log(error);
      };
      navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    },
    getWeather() {
      axios
        .get(
          "https://api.openweathermap.org/data/2.5/weather?lat="+this.lat+"&lon="+this.lon+"&appid="+process.env.VUE_APP_API_KEY
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
/*----- NAVBAR -----*/
.navbar {
  height: 56px;
  background: rgba(0, 128, 0, 0.13);
}
/*----- Main -----*/

.mainBody {background: #E5ECF4}
.mainContainer{
  margin: 0 48px;
  text-align:center;
}
.updatedIn{text-align: end;margin: 24px 0 -12px 0;cursor: pointer;}
.updatedIn:hover img{animation: boom 1s;}
.weatherIcon img{
  height: 200px;
  filter:drop-shadow(0 0 4px rgba(0, 0, 0, 0.15)) ;
}
.weatherCity{font-size:32px;color: #484848;height: max-content;}
.weatherCity img{height:26px; cursor:pointer;}
.mainTemperature {display: flex;justify-content: center;gap: 12px;margin-top: 28px;}
.mainTemperature .averageTemp {font-size: 36px;color: #242424;}
.mainTemperature .maxMinTemp :is(.maxTemp, .minTemp){display: flex;}
.mainTemperature :is(.maxMinTemp, .maxTemp)  i{font-style: normal;}
.mainTemperature .maxMinTemp .maxTemp i{color: #EC6E4C;}
.mainTemperature .maxMinTemp .minTemp i{color: #00BDF9;}
.tempTex{font-size: 32px;color: #242424;margin: 18px 0 28px 0;text-transform: capitalize;}
.cardsContainer{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(96px, 1fr));
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
  font-size: 14px;
  color: #363636;
}
.card p{
  font-weight: 500;
  font-size: 20;
  color: #444444;
  line-height: 400%;
}
.grid2{grid-column: 1/3;}


@keyframes boom{
  0%{
    filter:drop-shadow(0 0 0 rgba(0, 0, 0, 1));
  }
  100%{
    filter:drop-shadow( 0 0 20px rgba(0, 0, 0, 0));
    transform:rotate(360deg);
  }
}






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
