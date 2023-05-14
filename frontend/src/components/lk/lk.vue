<template>
  
  <div  class="wrapper">
  
 
     <div class="profil">
          <div class="profil__title">Аккаунт</div>
          <div class="profil__button">
                  <a  class="qqq" href="/info">
                  <button class="white">Редактировать</button>
                  </a>
                 
                  <a class="qqq" href="/owners">
                  <button class="black">Я владелец!</button>
                  </a>
              </div>
          <div class="profil__wrapper">
              
          
              <div class="profil__photo">
                <img class="" v-bind:src="profileData.photo" alt="">
  
              </div>
              <div class="profil__username">
                  <div class="profil__fio">
                    <div class="profil__username">
                      <div class="username1">Имя пользователя:</div>
                      <div class="username1">{{this.profileData.image}}</div>
                      <div class="username2">
                        <input type="text" v-model="profileData.fio">
                      </div>
  
                  </div>
                  
                  <div class="profil__username">
                      <div class="username1">Псевдоним:</div>
                      <div class="username2">
                        <input type="text" v-model="profileData.user.username">
                      </div>
  
                  </div>
                  <div class="profil__username">
                      <div class="username1">Email:</div>
                      <div class="username2">
                        <input type="text" v-model="profileData.user.email">
                      </div>
  
                  </div>
                  <div class="profil__username">
                      <div class="username1">Телефон:</div>
                      <div class="username2"> 
                        <input type="text" v-model="profileData.phone_num">
                      </div>
  
                  </div>
              </div>
  
          </div>
      </div>
    </div>  
    
  </div> 
 
 
 
  
  <wrapper_last_viewed  v-if=" shouldShowsimpleUserViewed" >
    
  </wrapper_last_viewed   >
  <wrapper_favourites v-if=" shouldShowsimpleUserViewed" > </wrapper_favourites>
  <vlad v-if=" shouldShowownerUserViewed" ></vlad>
  
      
  
     
     
    
  
  
  

    
  
  </template>
  


  <script >


import Info from '../../components/info/info.vue'
import wrapper_last_viewed    from '../../components/last_viewed/wrapper_last_viewed.vue'
import wrapper_favourites from '../favourites/wrapper_favourites.vue'
import axios from 'axios'

import { mapGetters } from 'vuex'



import { computed } from 'vue'


import vlad from '../../components/vlad/vlad.vue'
export default {
  name: 'profil',
  components:{
  wrapper_last_viewed,
  wrapper_favourites,
  vlad,
  },
 
  

 
  data(){
    return{
   
      profileData: {
        image: '',
        fio: '',
        username: '',
        email: '',
        phone: '',
        user: '',
        
      }
    
    
  
      
    }

  },

  computed: {
    isLoggedIn() {
      return this.$store.state.isLoggedIn;
      
    },
    shouldShowsimpleUserViewed() {
      return this.profileData.role === 'simple_user';
    },
    shouldShowownerUserViewed() {
      return this.profileData.role === 'owner_user';
    },
    
  },
  mounted() {
    //   , { withCredentials : true }
    axios.get('http://127.0.0.1:8000/api/v1/user/info')
      .then(response => {
        this.profileData = response.data;
        
      })

      .catch(error => {
        console.error(error);
      });
  },
  methods: {
    setLoggedIn(value) {
      this.isLoggedIn = value;
    }
  },
 
  
  
  

 

 
}
    
</script>


<style  scoped>


.wrapper {
  width: 1000px;
  margin: 0 auto;
  padding-top: 20px;
  padding-top: 20px;
  padding-right: 15px;
  padding-left: 15px;
  overflow: hidden;
  background-color: white;
  font-family: Arial, sans-serif;
  color: #333;
}

.profil__title{
  font-style: normal;
  font-weight: 400;
  font-size: 22px;
  line-height: 22px;
  padding-top: 53px;
  padding-left: 41px;
  }
  
  .profil__wrapper{
      display: flex;
      padding-bottom: 50px;
  }
  .profil__wrapper input{
    border: none;
    outline:none;
    box-shadow: none;
  }
  
  .profil__photo img{
      margin-left: 34px;
      margin-top:30px;
      width: 260px;
      height: 260px;
  
  }
  
  .profil__button{
      
  
      padding-left: 550px;
  }
  
  .white{
  cursor: pointer;
      width: 166px;
      height: 54px;
      background: #FFFFFF;
  border: 1px solid #000000;
  border-radius: 20px;
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  
  }
  
  .black{
      cursor: pointer;
     
      width: 166px;
      height: 54px;
      color: #FFFFFF;
      font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  background: #000000;
  border-radius: 20px;
  margin-left: 40px;
  
  }
  
  .profil__info{
      font-weight: 400;
      margin-left: 250px;
      font-size: 16px;
  line-height: 19px;
      
  }
  
  .profil__fio {
      padding: 40px 0px 0px 100px;
     
  }
  .profil__username{
      padding-top: 40px;
      display: flex;
  }
  
  .profil__email{
      padding-top: 40px;
      display: flex;
  }
  
  .profil__phone{
      padding-top: 40px;
      display: flex;
  }
  
  .fi02{
      padding-left: 121px;
  
  }
  .username2{
      padding-left: 82px;
  }
  .email2{
      padding-left: 121px;
  }
  .phone2{
      padding-left: 94px;
  }
  
  
  
  
  
  
  
  
  
  
  .lastComment{
      background: #D9D9D9;
  border-radius: 20px;
  width: 960px;
  min-height: 207px;
  margin: 0px 15px;
  }
  
  .lastComment__title{
      margin: 50px 0px;
      padding-left: 20px;
      font-weight: 400;
  font-size: 18px;
  line-height: 22px;
  }
  .lastComment__header{
      justify-content: space-between;
      padding: 15px 20px;
      display: flex;
      font-weight: 400;
      font-size: 16px;
      line-height: 19px;
  }
  
  .lastComment__discText{
  padding-right: 7px;
  }
  
  
  .header__name{
      padding-top: 12px;
  
  }
  .header__data{
      padding-top: 12px;
  }
  .header__image img{
      width: 40px;
      height: 40px;
  }
  
  .lastComment__discWrapper{
  
      display: flex;
      justify-content: space-between;
  }
  .lastComment__discImage img{
      border-radius: 20px;
      width: 450px;
      height: 275px;
  }
  
   .lastComment__discImage img:hover{
      transition: 1.2s;
      border-radius: 20px;
      width: 540px;
      height: 330px;
  
  } 
  .lastComment__disc{
  
      padding: 10px;
      margin: 20px 30px;
      width: 900px;
      min-height: 130px;
      background: #FFFFFF;
      border-radius: 20px;
  }
  
  .lastComment__wrapper:last-child{
      padding-bottom: 10px;
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  .object{
      background: #D9D9D9;
      height:600px ;
      border-radius: 20px;
  
  }
  
  .object__wrapper{
      display: flex;
      justify-content: space-around;
  }
  
  .object__title{
  font-weight: 400;
  font-size: 20px;
  line-height: 22px;
  padding: 50px 0px;
  text-align: center;
  }
  
  .object__card{
      margin-left: 5px;
      width: 286px;
      height: 444px;
      background-color: #fff;
      border-radius: 20px;
  }
  
  .card__photo{
      text-align: center;
      align-items: center;
      padding: 14px 0px;
  }
  
  .card__content{
      font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  color: #000000;
  }
  .card__name{
  text-align: center;
  }
  .card__reviews{
      padding-top: 27px;
      padding-left: 13px;
  
  }
  
  .card__rating{
      padding-top: 19px;
      padding-left: 13px;
  
  }
  
  .card__class{
  
  color:#7A7A7A;
  text-align: center;
  
  }
  
  
  .reviews__wrapper{
      background-color: #D9D9D9;;
      border-radius: 20px;
  }
  
  .reviews__title{
      font-weight: 400;
  font-size: 20px;
  line-height: 22px;
  padding: 30px 0px;
  text-align: center;
  
  }
  
  .reviews__header{
      padding: 15px 0px;
      display: flex;
      justify-content: space-around;
  }
  
  .reviews__text{
      padding: 10px 30px;
  
  }
  
  /* .photo__inreviews img {
      width: 500px;
      height: 440px;
      border-radius: 20px;
      border: 2px solid black;
      /* background-image: url('/img/reviewsphoto.jpg'); 
  } */
  
  
  .reviews__data{
      font-size: 15px;
      padding-top: 10px;
  }
  
  .reviews__text{
      min-height: 200px;
      display: flex;
      justify-content: space-between;
  }
  
  
  .photo__inreviews{
      width:100%;
      height: 100%;
  
  }
  
  .photo__inreviewsdiv{
      width:100%;
      height: 100%;
  
  }
  
  .photo__inreviews:hover{
      z-index: 10;
      width: 500px;
      height: 500px;
  }
  
  
  
  
  
 
  

  
  a {
    text-decoration: none;
    color: #3498db;
  }
  
  .container1{
    max-width: 1000px;
    padding: 0px 5px;
    overflow: hidden;
  }
  
  
  h1{
    padding: 20px 0px;
    position: relative;
  }
  
  .photo__inreviews{
      align-items: center;
      text-align: center;
      justify-content: center;
  }
  
  .photo__inreviewsdiv{
      margin: 0 auto;
      align-items: center;
      text-align: center;
  }
  
  .photo__inreviews{
      width: 40%;
      height: 30%;
  }
  
  
  
  



</style>