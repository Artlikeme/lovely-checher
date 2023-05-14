<template>
  <div class="wrapper">
    <div class="section_3">
      <div class="section_3_left">
      <button class="tablinks"  @click="openCity($event, 'location_information_rest')"  >
     общая информация
    </button>
    
    <button class="tablinks"  @click="openCity($event, 'card_location_rest')"   >
       на карте
    </button>
    <button  class="tablinks" @click="openCity($event, 'menu_rest')">
     меню
    </button>
    <button class="tablinks" @click="openCity($event, 'to_book_rest')">
      забронировать столик
    </button>
    </div>
    <div  id="location_information_rest" class="location_information_rest tabcontent " >
  
      <ul>
        
        <li>Адрес: {{object.address}}</li>
        <li>Часы работы:{{object.opening_hours}}</li>
        <li>Телефон: {{object.telephone}}</li>
        <li>цена:{{object.  prace}}</li>
        <li>Парковка: {{object.parking}}</li>
      </ul>
    
  </div>

  <div  id="menu_rest" class="menu_rest tabcontent" >
   
    <carousel class="carousel" :items-to-show="1.5">
      <slide class="slide" v-for="slide in 10" :key="slide">
        {{ slide }}
      </slide>
  
      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
  </div>

  <div id="to_book_rest" class="to_book_rest tabcontent">
  
    <ul class="list">
        <li><button  class="button choice-button" @click="buttonClicked(1)">1</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(2)">2</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(3)">3</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(4)">4</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(5)">5</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(6)">6</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(7)">7</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(8)">8</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(9)">9</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(10)">10</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(11)">11</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(12)">12</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(13)">13</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(14)">14</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(15)">15</button></li>
        <li><button class="button choice-button" @click="buttonClicked(16)">16</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(17)">17</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(18)">18</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(19)">19</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(20)">20</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(21)">22</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(22)">22</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(23)">23</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(24)">24</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(25)">25</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(26)">26</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(27)">27</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(28)">28</button></li>
        <li><button  class="button choice-button" @click="buttonClicked(29)">29</button></li>
    </ul>
    <div class="list-inner">
      <h3>Забронировать столик № {{buttonValue}}</h3>
       
        <button class="button">Да</button>
    </div>

  </div>
  <div  id="card_location_rest" class=" card_location_hotel tabcontent" >

    <iframe id="map"   src="https://yandex.ru/map-widget/v1/?um=constructor%3Afa21781a38912061c4184a7fb8238148c995dadca8728c94f0c649f2a949ce76&amp;source=constructor" width="663" height="356" frameborder="0" ></iframe>
    
  </div>
  
  </div>
  </div>
  

</template>

<script>
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

 export default {
  name: 'card_changeable_rest',
  components:{
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  props: {
    object: {
      type: Object
    },
  },
  data(){
    return{
      buttonValue: '',
    
     
      

  
      
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
    buttonClicked(value) {
    this.buttonValue = value;
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
  max-width: 920px;
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
  width: 240px;
  height: 90px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.tablinks{
  background: white;
  border-radius: 20px;
  border: none;
  width: 240px;
  height: 90px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.tablinks{
  background: white;
  border-radius: 20px;
  border: none;
  width: 240px;
  height: 90px;
  cursor: pointer;
  transition: background linear 0.5s;
}
.tablinks{
  background: white;
  border-radius: 20px;
  border: none;
  width: 240px;
  height: 90px;
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
.tablinks:hover{
  background-color: black;
  color:white;
}
.location_information_rest{
  margin-right: 50px;
}
.location_information_rest li{
  list-style-type:none;/*убираем точки*/
  margin-bottom:20px ;
}
.menu_rest{
  margin: auto;
 
  width: 800px;
  box-sizing: border-box;
}
.carousel{
  width: 680px;
  

}




.list button{

 
  border: none;
  color:black; 
  padding: 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 50%;
  outline: none;
  position: relative;
  overflow: hidden;
  background: none;
  transition: 0.5s;
}


.list
{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  
}




.people-input{
    border: none;
    font-size: 25px;
    width: 30px;
    font-weight:bold;
}


.list-inner{
  display: flex;
  align-items: center;
  text-align: center;
  margin-left: 150px;
 
}
.button{
  padding: 20px;
  border: none;
  margin-left: 30px;
  border-radius: 45%;
  cursor: pointer;
  transition: background linear 0.5s;
  background-color: #BCBBBB;

}
.button:hover {
  background-color:black;
  color:white;
}











.tabcontent  {
  display: none;

}

#map{
 
  border-radius: 19px;
}










</style>