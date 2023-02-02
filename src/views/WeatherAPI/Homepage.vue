<template>
    <div>
        something
        <button @click="getCoordinates">try get API</button>
    </div>
</template>
<script>
import { integer } from 'vscode-languageserver-types';
import axios from 'axios'
export default {
    name:'WeatherHome',
    data() {
        return {
            apiKeyLink:'https://home.openweathermap.org/api_keys',
            userInputs:{city:String, stateCode:integer, countryCode:integer},
            
        }
    },
    methods: {
        getCoordinates(userInputs){
            var limit = 1
            const apiKey = "random"
            const apiCall = "http://api.openweathermap.org/geo/1.0/direct?q="+ userInputs.city +","+ userInputs.stateCode +","+ userInputs.countryCode +"&limit="+ limit +"&appid="+ apiKey

            axios
                .get(apiCall)
                .then((response) => {
                    console.log(response.data)
                });
        }     
    },
}
</script>