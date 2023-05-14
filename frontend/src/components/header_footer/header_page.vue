<template>
  <!-- Header_first -->
  <div class="header-wrapper_header_first">
    <div class="container">
 
    <div class="header-first">
     
      <H3> <Router-link class="router-link_main_page" to="/">Lovely Checker</Router-link></H3>
      <div class="form">
      <input   v-model="searchText" @focus="onFocus" @blur="onBlur" :style="{ width: inputWidth }"   class="form__input" type="search" placeholder="Искать на Lovely Checker">
      <button   @click="sendData" class="form__link"><img  src="../../assets/search_header.svg" alt="#"></button>
       </div>
       
      <select v-model="selectedCity" @change="sendData"  id="selectID_2">
        <option value="">Выбор города</option>
        <option v-for="city in cities" :key="city.id" :value="city.id">{{ city.name }}</option>
        
        
        </select>
     
        <div class="profile">
          <button class="auth-btn_exit" v-if="!isLoggedIn">
            <a href="/login">Войти</a>
          </button>
          <button class="auth-btn" v-else>
            <a href="/personal-account">Выйти</a>
          </button>


          
        </div>
        <div class="personal_acc">

          <button class="auth-btn_lk" >
            <a href="/profil   ">Личный кабинет</a>
          </button>
         


        </div>
     
    </div>
  </div>
</div>
 
  <!-- header second -->
  
  <div class="header-wrapper_header_second">
    <div class="container">

    <div class="header-second">
   
      <ul>
        <li><div class="header_second_li"> <router-link to="/card_catalog_theater_wrapper">Театры/Кино</router-link></div></li>
          <li><div class="header_second_li"><router-link to="">Музеи/Галереи</router-link></div></li>
          <li><div class="header_second_li"><router-link to="/card_catalog_parks_wrapper">Парки/Скверы</router-link></div> </li>
          <li><div class="header_second_li"><router-link to="/card_catalog_rest_wrapper">Кафе/Рестораны</router-link></div></li>
          <li><div class="header_second_li"><router-link to="/card_catalog_hotel_wrapper">Отели</router-link></div></li>
          <li><div class="header_second_li"><router-link to="">Другое</router-link></div></li>
        </ul> 
      </div>
    </div>
  </div>
  

</template>

<script>
import axios from 'axios';
export default{
  name:'header_page',
  data() {
    return {
      searchText: '',
      selectedCity: '',
      inputWidth: '400px',
      cities: [],
  
    }
  
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/v1/main/')  //геттер на получение города с API
      .then(response => {
        this.cities = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  },


  methods: {
    sendData() {
      axios.get(`http://127.0.0.1:8000/api/v1/item/search?search=${this.searchText}`, {
  // отправка текста и id города на API 
  search: this.searchText,
  cityId: this.selectedCity
})
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.log(error);
      });
    },
    onFocus() {
      this.inputWidth = '300px';
    },
    onBlur() {
      this.inputWidth = '350px';
    },
    handleClickOutside(event) {
      if (!this.$el.contains(event.target)) {
        this.inputWidth = '350px';
      }
    },
  
  }
}



</script>



<style scoped>
.container
{
  width:100%;
  max-width: 1200px;
  margin: 0 auto;
}


.header-wrapper_header_first{
  width:1354px;
 background-color: #E3DDFF;
  overflow: hidden;
  margin: 0 auto;
  border-radius: 20px;
}

.header-wrapper_header_second{
  width:1354px ;
  background-color: #CFC7F8;
  overflow: hidden;
  margin: 0 auto;
  border-radius: 20px;
}

.header-first{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 0 auto;
  max-width:1000px ;
  max-height: 74px;
}

.header-second{
  background-color: #CFC7F8;
  max-width: 1000px;
  margin: 0 auto;
 max-height:64px ;
}

.header_second_li  a { 
  width: 157px;
  height:  29px;
 border-radius: 20px;
  background-color: #CFC7F8 ;
  text-align: center;
  padding: 10px;
  cursor: pointer;
  transition: background linear 0.5s;
}

.header_second_li a:hover {
  background-color:black;
  color:white;
}

.header-second ul{
  display: flex;
  text-align: center;
  margin-left:35px ;
  margin-right: 35px;
  justify-content: space-between;
  list-style-type:none;/*убираем точки*/
}

.header-second a{
  text-decoration: none;
  color: #000000;
}

.form{
  position: relative;
  display: flex;
  align-items: center;
}

.form__input{
  outline:none;
  border:none;
  width: 300px;
  height: 30px;
  border-radius: 20px;
  padding-left: 30px;

    transition: width 0.3s;
  
}
.form__link{
  background-color:transparent ;
 border: none;
 height: 30px;
  background-repeat: no-repeat;
  right: 0px;
  position: absolute;
}

#selectID_2{
  background-color: #CFC7F8;
  outline:none;
  border:none;
 
  height: 30px;
  border-radius: 20px;
}

.profile{
  display: flex;
  align-items: center;
  background-color:#CFC7F8;
  width: 95px;
  height: 30px;
  border-radius: 35px;
  
}
.personal_acc{
  display: flex;
  
  background-color:#CFC7F8;
  
  border-radius: 35px;
}

#selectID{
  width: 15px;
  height: 13.42px;
  border-radius: 20px;
  border: none;
  
  background-color:#CFC7F8;
  outline:none;
}

.profile-img{
  width: 30px; 
height: 30px;
background: rgba(102, 102, 102, 1);
border-radius: 50%;
margin-right: 5px;
margin:0px 22px 0px 10px;
}
.router-link_main_page{
  text-decoration:none;
  color: black;
}
.auth-btn_exit{
  border-radius: 35px;
  width: 95px;
    height: 30px;
    background-color: #CFC7F8;
    outline: none;
    border: none;
}
.auth-btn_exit a{
  color: black;
  text-decoration:none;
}
.auth-btn_lk a{
  color: black;
  text-decoration:none;
}
.auth-btn_lk{
  background-color: #CFC7F8;
  outline: none;
  border: none;
  border-radius: 35px;
  height: 30px;
}


</style>