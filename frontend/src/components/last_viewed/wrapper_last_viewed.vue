<template>
 
   <div   class="wrapper">
    <h3>Последнии просматриваеммые объекты</h3>
   <catalog_last_viewed/>
  </div>
  
 







</template>


<script>

import catalog_last_viewed from './catalog_last_viewed.vue'
export default {
  name:'wrapper_last_viewed',

  components: {

catalog_last_viewed
    
    
    
   
   
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
  background-color: #E3DDFF;

}
 .wrapper h3{
   margin-top: 0px;
   text-align: center;
   
 }


</style>