<template>
  <div class="wrapper">
    <div class="section_3">
      <div class="section_3_left">
      <button  class="tablinks"  @click="openCity($event, 'location_information_hotel')"  >
     общая информация
    </button>
    
    <button class="tablinks"  @click="openCity($event, 'card_location_hotel')"   >
       на карте
    </button>
    <button class="tablinks" @click="openCity($event, 'registr_theater')" >
      Зарегистрироваться
    </button>
    
    
    </div>
    <div   id="location_information_hotel" class="tabcontent location_information_hotel" >
  
      <ul>
        <li>Адрес: {{object.address}}</li>
        <li>Часы работы:{{object.opening_hours}}</li>
        <li>Телефон: {{object.telephone}}</li>
        <li>средняя цена за номер:{{object.  price_list_for_hotels}}</li>
        <li> Наличие Парковки: {{object.parking}}</li>

        
      </ul>
    
  </div>
  <div  id="registr_theater" class="reg tabcontent">
    <div class="date_of_register_wrapper">
      <p>Зарегистрироваться</p>
    <datepicker class="check_in_hotel_1"
        v-model="selectedDate_check_in_hotel" 
        format="dd.MM.yyyy" 
        language="ru">
      </datepicker>
    </div>
    <div class="exit_hotel_wrapper">
      <p>Выезд</p>
      <datepicker class="exit_hotel_1"
      v-model="selectedDate_exit_hotel" 
      format="dd.MM.yyyy" 
      language="ru">
    </datepicker>
   </div>
   <div class="number_of_persons_wrapper">
    <p>Количество персон</p>
    <div class="number_of_persons">
      
      <img class="person" src="../assets/card_changeable/person.svg" alt="">
      <input class  v-model="count" />
      
      <button class="arrow_left" @click="decrement"><img  src="../assets/card_changeable/arrow_left.svg" alt=""></button>
      <button class="arrow_right" @click="increment" ><img  src="../assets/card_changeable/arrow_right.svg" alt=""></button>
    
    </div>
  </div>
  <div class="button_take_off_wrapper">
    <button class="button_take_off">
      забронировать
    </button>
  </div>
     
  
  </div>
  <div  id="card_location_hotel" class=" card_location_hotel tabcontent" >

  <iframe id="map"   src="https://yandex.ru/map-widget/v1/?um=constructor%3Afa21781a38912061c4184a7fb8238148c995dadca8728c94f0c649f2a949ce76&amp;source=constructor" width="663" height="356" frameborder="0" ></iframe>
  
</div>
  
  </div>
  </div>


</template>


<script>

import Datepicker from 'vue3-datepicker'
 export default {
  name: 'card_changeable_hotel',
  props: {
    object: {
      type: Object
    },
  },
  components:{
    
    Datepicker
 
  },
  data(){
    return{
      
      
      selectedDate_check_in_hotel: null,
      selectedDate_exit_hotel:null,
      count: 0

     
  
  
      
    }

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
    },
    increment() {
      this.count++
    },
    decrement() {
      this.count--
    }
    
  },
 
  
 
}

</script>


<style  >

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
  width: 256px;
  height: 178px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.tablinks{
  background: white;
  border-radius: 20px;
  border: none;
  width: 256px;
  height: 178px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.tablinks{
  background: white;
  border-radius: 20px;
  border: none;
  width: 256px;
  height: 178px;
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
  background-color:black;
  color:white;
}

.location_information_hotel li{
  list-style-type:none;/*убираем точки*/
  margin-bottom:20px ;
}




.reg{
  display: grid;
  row-gap: 20px;
  margin:0 auto;
  padding-top: 25px;

}

.check_in_hotel_1{
  width: 149px;
  height: 46px;
  border-radius: 20px;
  border: 1px solid black;
  padding-left: 30px;
   

}
.exit_hotel_1{
  width: 149px;
  height: 46px;
  border-radius: 20px;
  border: 1px solid black;
  padding-left: 30px;
}
.number_of_persons input{
  width: 149px;
  height: 46px;
  border-radius: 20px;
  border: 1px solid black;
  padding-left: 30px;
  outline: none;
}
.number_of_persons{
  position: relative;
  display: flex;
  align-items: center;
}
.person{
  background-color: transparent;
    border: none;
    height: 30px;
    background-repeat: no-repeat;
    left: 4px;
    position: absolute;
}
.arrow_left{
  background-color: transparent;
    border: none;
    height: 30px;
    background-repeat: no-repeat;
    right: 26px;
    position: absolute;
    
}
.arrow_right{
  background-color: transparent;
    border: none;
    height: 30px;
    background-repeat: no-repeat;
    right: 0px;
    position: absolute;
}
.button_take_off {
  background: white;
    border-radius: 20px;
    border: none;
    width: 140px;
    height: 60px;
    cursor: pointer;
    transition: background linear 0.5s;
}
.button_take_off:hover{
  background-color:black;
  color:white;
}

.button_arrow{
  position: absolute;
}
.date_of_register_wrapper{
  display: flex;
 gap: 20px;
 align-items: center;
}
.exit_hotel_wrapper{
  display: flex;
  gap: 20px;
  align-items: center;
}
.number_of_persons_wrapper{
  display: flex;
  gap: 20px;
  align-items: center;
}
.button_take_off_wrapper{
  display: flex;
  justify-content: center;
  align-items: center;
} 
.tabcontent {
  display: none;
 
}
#map{
 
  border-radius: 19px;
}

</style>