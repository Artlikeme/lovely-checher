<template>
  <div  class="card_catalog">

      <div class="catalog_list">
          <item_last_viewed
              v-for="product in  LAST_VIEWED   "
              :key="product.id"
              :product_data="product"
              :number="product.rating"
          />
      </div>


  </div>


</template>

<script>


import LAST_VIEWED from 'axios'
import {mapActions, mapGetters} from 'vuex'
import item_last_viewed from './item_last_viewed.vue'


export default {
  name: 'catalog_last_viewed',
  components: {
      item_last_viewed,
  },
  data() {
      return {}
  },
  computed:{
    ...mapGetters([
 'LAST_VIEWED'
    ]),
  },
  methods: {
  
    
    ...mapActions([
      'GET_LAST_VIEWED_FROM_API'
      ]),

  },
  mounted(){
    this.GET_LAST_VIEWED_FROM_API()
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