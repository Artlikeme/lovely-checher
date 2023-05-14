<script setup>
import { computed, reactive } from 'vue'
import axios from 'axios'


const OwnersConfir = reactive({
  fio: '',
  username: '',
  email: '',
  phone: '',
  INN: '',
  OGRN: '',

})

const submit = () => {
  console.log('submit');
  axios.post('/',OwnersConfir).then((response) =>{
    console.log(response)

  }).catch((error) =>{
    console.log(error)
  })
}






</script>

<template>
  <div class="wrapper">
    <div class="wrapper_owners">
<form
@submit.prevent.stop = "submit"
>
    <div class="title">Личные данные для подтверждения <br>собсвтенности объектов</div>
    <div class="form-group">
    <label for="exampleInputEmail2">ФИО</label>
    <input 
    v-model="OwnersConfir.fio"
    type="text" class=" mt-2 form-control"  id="exampleInput" aria-describedby="emailHelp" 
    placeholder="Сталоне Сильвестр Александрович">
   
  </div>
  <div class="form-group">
    <label for="exampleInputEmail2">Псевдоним</label>
    <input 
    v-model="OwnersConfir.username"
    type="text" class=" mt-2 form-control"  id="exampleInput" aria-describedby="emailHelp" 
    placeholder="RACE">
   
  </div>
  <div class="form-group">
    <label for="exampleInputEmail2">Email</label>
    <input 
    v-model="OwnersConfir.email"
    type="email" class=" mt-2 form-control"  id="exampleInput" aria-describedby="emailHelp" 
    placeholder="Example@yandex.ru">
   
  </div>
  <div class="form-group">
    <label for="exampleInputEmail2">Телефон</label>
    <input 
    v-model="OwnersConfir.phone"
    type="text" class=" mt-2 form-control"  id="exampleInput" aria-describedby="emailHelp" 
    placeholder="88888888888">
   
  </div>
  <div class="form-group">
    <label for="exampleInputEmail2">ИНН</label>
    <input 
    v-model="OwnersConfir.INN"
    type="text" class=" mt-2 form-control"  id="exampleInput" aria-describedby="emailHelp" 
    placeholder="6163027810">
   
  </div>
  <div class="form-group">
    <label for="exampleInputEmail2">ОГРН</label>
    <input 
    v-model="OwnersConfir.OGRN"
    type="text" class=" mt-2 form-control"  id="exampleInput" aria-describedby="emailHelp" 
    placeholder="1026103165241">
   
  </div>

  <button type="submit" class="button">Отправить на проверку</button>

  
</form>
</div>
</div>
</template>

<style scoped>
.wrapper_owners {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 30px 0px 30px 0px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #F3F0FF;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.1);
  width: 400px;
}

.title {
  text-align: center;
  font-size: 26px;
  font-weight: 700;
}

.form-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

label {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 10px;
}

input {
  height: 45px;
  border-radius: 10px;
  border: 1px solid #ccc;
  padding: 10px;
  font-size: 16px;
  width: 100%;
  margin-bottom: 20px;
}

.button {
  padding: 9px;
  background-color: #CFC7F8;
  width: 100%;
  font-size: 1rem;
  border-radius: 15px;
  border: #CFC7F8;
  color: black;
  font-weight: 600;
  transition: all 0.2s ease-in-out;
}



.button:hover {
  cursor: pointer;
  opacity: 0.8;
  background-color:black;
  color:white
}

.text {
  text-align: center;
}

.text__checker {
  font-size: 16px;
  color: #4d4d4d;
  text-decoration: underline;
  transition: all 0.2s ease-in-out;
}

.text__checker:hover {
  cursor: pointer;
  color: black;
}
</style>