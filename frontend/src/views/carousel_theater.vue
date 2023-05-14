<template>
  <div class="wrapper">
    <div class="section_3">
      <div class="section_3_left">
        <button class="tablinks"  @click="openCity($event, 'location_information_theater')">
          общая информация
        </button>
    
        <button class="tablinks"  @click="openCity($event, 'card_location_theater')">   
          на карте
        </button>
    
        <button class="tablinks" @click="openCity($event, 'event_theater')"> 
          предстоящие мероприятия
        </button>
      </div>

      <div id="location_information_theater" class="location_information_theater  tabcontent ">
        <ul class="location_information_rest">
          <li>Адрес: {{object.address}}</li>
          <li>Часы работы: {{object.opening_hours}}</li>
          <li>Телефон: {{object.telephone}}</li>
          <li>Дана основания: {{object.date_of_foundation}}</li>
        </ul>
      </div>

      <div id="event_theater" class=" event_theater tabcontent">
        <img :src="object.event" alt="Event Image">
      </div>
      <div  id="card_location_theater" class=" card_location_hotel tabcontent" >

        <iframe id="map"   src="https://yandex.ru/map-widget/v1/?um=constructor%3Afa21781a38912061c4184a7fb8238148c995dadca8728c94f0c649f2a949ce76&amp;source=constructor" width="663" height="356" frameborder="0" ></iframe>
        
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'card_changeable_theater',
  components: {},
  props: {
    object: {
      type: Object
    },
  },
  data() {
    return {}
  },
  methods: {
    openCity(evt, cityName) {
      // Declare all variables
      var i, tabcontent, tablinks;

      // Get all elements with class="tabcontent" and hide them
      tabcontent = document.getElementsByClassName("tabcontent");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }

      // Get all elements with class="tablinks" and remove the class "active"
      tablinks = document.getElementsByClassName("tablinks");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
      }

      // Show the current tab, and add an "active" class to the button that opened the tab
      document.getElementById(cityName).style.display = "block";
      evt.currentTarget.className += " active";
    }
  }
}

</script>

<style scoped>
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



.tablinks{
  background:white;
  border-radius: 20px;
  border: none;
  width: 305px;
  height: 119px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.tablinks{
  background: white;
  border-radius: 20px;
  border: none;
  width: 305px;
  height: 119px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.tablinks{
  background: white;
  border-radius: 20px;
  border: none;
  width: 305px;
  height: 119px;
  cursor: pointer;
  transition: background linear 0.5s;
}

.tablinks:hover {
  background-color:black;
  color:white;
}

.tablinks:hover{
  background-color:black;
  color:white;
}
.tablinks:hover{
  background-color: black;
  color:white;
}

.location_information_theater li{
  list-style-type:none;/*убираем точки*/
  margin-bottom:20px ;
}
.tabcontent {
  display: none;
 
}

#map{
 
  border-radius: 19px;
}

</style>