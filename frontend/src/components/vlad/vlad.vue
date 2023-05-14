<script >


import { computed, reactive, } from 'vue'
import news from '../../components/news_vlad/news.vue'
import axios from 'axios'

export default {
   
    components: {
       news
    },
 

}






</script>

<template>

   
     
    <div class="object__wrapper">
        <div class="object__news">
        </div>
    </div>
<news></news>
<div class="wrapper">
<div class="my">
    <div class="my__title"></div>
    <div class="my__wrapper">
        <div class="object__card__wrappe">
       
          </div>
            <div class="object__card__new">
                <div class="new__card">
                    <a href="/form">
            <div class="new__alt__crug">
                
                
</div>
</a>
<p class="photo__center">Добавить новый</p>

</div>

            </div>
    </div>

</div>
</div>



   




</template>

<style scoped>


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
    position: absolute;
    width: 166px;
    height: 54px;
    color: #FFFFFF;
    font-style: normal;
font-weight: 400;
font-size: 16px;
line-height: 19px;
background: #000000;
border-radius: 20px;
left:40px
}

.profil__info{
    font-weight: 400;
    margin-left: 250px;
    font-size: 16px;
line-height: 19px;
    
}

.profil__fio {
    padding-top: 40px;
    display: flex;
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

.my__title{
    padding-top: 49px;
    padding-left: 39px;
    font-style: normal;
font-weight: 400;
font-size: 18px;
line-height: 22px;
padding-bottom: 25px;
}


.my{
  width: 100%;
    margin: 40px 0px;
    background: #CFC7F8;
    height: 600px;
    border-radius: 20px;
}

.my__wrapper{
    display: flex;
    justify-content: center;
    padding: 10px;

   
}
.object__card{
    margin: 0px 10px;
    width: 286px;
    height: 444px;
    background-color: #fff;
    border-radius: 20px;
}
.object__card__new{
    margin: 0px 10px;
    width: 286px;
    height: 444px;
     background: #A4A4A4;

    border-radius: 20px;
}

.new__card{
 

margin: 0px auto;
background-color: white;
border-radius: 20px;
position: relative;
padding: 145px 0px;
}

.new__alt__crug{
    display: flex;
    --b: 4px; /* the thickness */
  width: 60px; /* the size */
  aspect-ratio: 1;
  border: 10px solid #CFC7F8; /* the outer space */
  background: conic-gradient(from 90deg at var(--b) var(--b),
  #CFC7F8 90deg,#fff 0) calc(100% + var(--b)/2) 
  calc(100% + var(--b)/2)/ calc(50% + var(--b)) calc(50% + var(--b));

  justify-content: center;
  align-items: center;
  text-align: center;
margin: 0px auto;
border-radius: 50%;


}


.statistic{
    background-color: #D9D9D9;
    height: 500px;
    border-radius: 20px;
}
.statistic__title{
    padding-top: 49px;
    padding-left: 39px;
    font-style: normal;
font-weight: 400;
font-size: 18px;
line-height: 22px;
padding-bottom: 35px;
}

.person__info{
  width: 100%;
  margin: 15px 0px;
  padding: 0px 250px;
  justify-content: space-between;
  font-size: 16px;

}



@media (max-width: 992px){
    .my__wrapper{
    display:block;
    flex-direction: column;
}
.card__item{
  padding: 15px 0px;
}


.object__card{
display: block;
margin: 0 auto;
}
.object__card__new{
display: block;
margin: 0 auto;
}
.object__card__wrapper{
    margin-top: 15px
}

.content-profile-page {
  width: 40em;

    }
    .avatar{
    margin: 0 246.7px;
}
}

@media(max-width:768px){
    .content-profile-page {
  width: 30em;
  

}
.avatar{
    margin: 0 189.7px;
}
}

@media(max-width:526px){
    .content-profile-page {
  width: 16.9em;

}
.person__info{
  width: 100%;
  margin: 5px 0px;
  padding: 0px 20px;

  font-size: 16px;

}
.avatar{
    margin: 0 73.5px;
}

}

</style>