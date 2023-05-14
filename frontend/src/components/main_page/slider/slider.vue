
<template>
  <div class="wrapper">
    
    <carousel class="carousel" :items-to-show="1.5">
      <slide class="slide" v-for="image in images" :key="image.id">

        <img :src="image.image " style="
 
        " alt="photo" />
      </slide>

      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
  </div>
</template>

<script>
import axios from 'axios';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'Slider',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  data() {
    return {
      images: [],
    };
  },
  methods: {
    fetchImages() {
      axios
        .get('http://localhost:8000/api/v1/news/topthree')
        .then(response => {
          this.images = response.data;
        })

        .catch(error => {
          console.log(error);
        });
    },
    ...mapActions(['GET_PRODUCTS_NEW_FROM_API']),
  },
  mounted() {
    this.fetchImages();
  },
};
</script>
<style scoped>

.slide{
  
 

  height: 400px;
 
  width: 840px;
  font-size: 20px;
  
  display: flex;
  justify-content: center;
  align-items: center;
  
}
.slide img{
  width: 100%;
  height: 100%;
  object-fit:  cover;
}
.carousel{
  border-radius: 20px;
  background-color:#CFC7F8;
  padding: 15px;
  margin-bottom: 100px;
  background-size: cover;
}


</style>