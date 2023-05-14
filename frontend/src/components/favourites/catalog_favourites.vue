<template>
  <div class="card_catalog">

      <div class="catalog_list">
          <item_favourites
              v-for="product in  FAVOURITES   "
              :key="product.id"
              :product_data="product"
              :number="product.rating"
          />
      </div>


  </div>


</template>

<script>


import FAVOURITES from 'axios'
import {mapActions, mapGetters} from 'vuex'
import item_favourites from './item_favourites.vue'


export default {
  name: 'catalog_favourites',
  components: {
      item_favourites,
  },
  data() {
      return {}
  },
  computed:{
    ...mapGetters([
 'FAVOURITES'
    ]),
  },
  methods: {
  
    
    ...mapActions([
      'GET_FAVOURITES_FROM_API'
      ]),

  },
  mounted(){
    this.GET_FAVOURITES_FROM_API()
  }



}


</script>


<style>

.catalog_list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;


}


</style>