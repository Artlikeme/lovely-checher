<template>
  
   <div class="wrapper ">
    <h3>Избранное</h3>
   <catalog_favourites/>
  
  </div>







</template>


<script>

import catalog_favourites from './catalog_favourites.vue'
export default {
  name:'wrapper_favourites',
  
  components: {

catalog_favourites
    
    
    
   
   
  },
}





</script>


<style scoped>

.wrapper {
  width: 1000px;
  margin: 0 auto;
  padding-top: 20px;
  padding-top: 20px;
  padding-right: 15px;
  padding-left: 15px;
  overflow: hidden;
 
}
 .wrapper h3{
   margin-top: 0px;
   text-align: center;
   
 }

</style>