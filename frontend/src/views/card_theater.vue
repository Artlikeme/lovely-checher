<template>
    <div class="card_theater">
        <place_info   :number="object.rating" :object="object"/>

        <carousel_theater v-if="object.category === 'Theatre/Cinema'|| object.category === 'Parks/Squares'"  :is="theaterComponent"  :object="object"/>
        <carousel_hotel v-if="object.category === 'Hotel'" :is="hotelComponent" :object="object"/>
        <carousel_rest v-if="object.category === 'Cafe/Restaurant'" :is="restComponent" :object="object"/>

        <app_comment :objects="object.comments"/>
    </div>


</template>


<script>
import carousel_rest from '../views/carousel_rest.vue';
import carousel_hotel from './carousel_hotel.vue';
import app_comment from '../components/comment/app_comment.vue'
import axios from "axios";
import place_info from "../components/card_object/place_info.vue";
import carousel_theater from '../views/carousel_theater.vue'

export default {

    name: 'card_theater',
    components: {
        place_info,
        carousel_theater,
        carousel_hotel,
        app_comment,
        carousel_rest


    },
    data() {
        return {
          object: {},
        }
    },
    props: {
    
  },

    computed: {
        ratingWidth() {
            return this.number / this.starLimit * 100
        },
        ratingWidthStyle() {
            return `width: ${this.ratingWidth}%;`
        }
    },
    created() {
        // this.object = "sdffs"
        const pk = this.$route.params.pk;
        if (pk === "undefined") {
            const pk = 1;
        }
        console.log(pk)
        axios.get(`http://127.0.0.1:8000/api/v1/item/${pk}`).then((response) => {
            this.object = response.data;
            // console.log(this.object);
        });
    },

}


</script>


<style>


</style>