<template>
<!-- <div class="wrapper">
  <div class="section_3">
    <div class="section_3_left">
    <button class="button-info" @click="button_info"  >
   общая информация
  </button>
  
  <button class="button-map " @click="button_map"   >
     на карте
  </button>
  <button class="button-event" @click="button_event">
    предстоящие мероприятия
  </button>
  </div>

 <location_information_theater
 
 v-if="is_open_info"
 :object="object"

 

 
 
 />
  <card_location
  v-if="is_open_card_location"
  :object="object"
  />
  
<event_theater

  v-if="is_open_event"
  :object="object"

  />
</div>
</div> -->


</template>


<script>
// import card_location from'../card_location.vue'
//  import location_information_theater from './locatin_information_theater.vue'
//  import event_theater from './event_theater.vue'
//  export default {
//   name: 'card_changeable_theater',
//   components:{
//    location_information_theater,
//    card_location,
//    event_theater
//   },
//   props: {
//         object: {
//             type: Object
//         },
//     },
//     data() {
//     return {
//       is_open_info: false,
//       is_open_card_location: false,
//       is_open_event: false
//     }
//   },
 
 
//     methods:{
//       button_map(){
//       this.is_open_card_location=!this.is_open_card_location;
      
//     },
//     button_info(){
//       this.is_open_info=!this.is_open_info;
//     },
//     button_event(){
//       this.is_open_event=!this.is_open_event;
//     }
//   },
// }
 

</script>


<!-- <style scoped>

.wrapper{
  width : 1000px;
   margin: 0 auto;
   padding-top: 20px;
   padding-top: 20px;
   padding-right: 15px;
   padding-left: 15px;
   overflow:hidden ;
   background-color: white;
 }
.section_3{
  width: 920px;
 height: 356px;
 border-radius: 20px;
 border:1px solid black;
 display: flex;
 margin: 0 auto;
}
.section_3_left{
  display: flex;
flex-direction: column
}



.button-info{
  background:white;
  border-radius: 20px;
  border: none;
  width: 305px;
  height: 119px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.button-map{
  background: white;
  border-radius: 20px;
  border: none;
  width: 305px;
  height: 119px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.button-event{
  background: white;
  border-radius: 20px;
  border: none;
  width: 305px;
  height: 119px;
  cursor: pointer;
  transition: background linear 0.5s;
}

.button-info:hover {
  background-color:black;
  color:white;
}

.button-map:hover{
  background-color:black;
  color:white;
}
.button-event:hover{
  background-color: black;
  color:white;
}




</style> -->