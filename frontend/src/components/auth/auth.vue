<template>
  <div class="wrapper">
    <form class="authorization__form" @submit.prevent.stop="submit">
      <div class="title">Регистрация</div>
      <div class="form-group">
        <label for="exampleInputEmail1">Email</label>
        <input
          v-model="Authorization.email"
          type="email"
          class="mt-2 form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          placeholder="example@email.com"
        >
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Псевдоним</label>
        <input
          v-model="Authorization.username"
          type="text"
          class="mt-2 form-control"
          id="exampleInputPassword1"
          placeholder="RISE"
        >
      </div>
      <div class="form-group">
        <label for="exampleInputPassword2">Пароль</label>
        <input
          v-model="Authorization.password"
          type="password"
          class="mt-2 form-control"
          id="exampleInputPassword2"
          placeholder="********"
        >
      </div>
      <div class="form-group">
        <label for="exampleInputPassword3">Повторите пароль</label>
        <input
          v-model="Authorization.repeatpassword"
          type="password"
          class="mt-2 mb-2 form-control"
          id="exampleInputPassword3"
          placeholder="********"
        >
      </div>
      <button type="submit" class="button" >
        Зарегистрироваться
      </button>
      <div class="text">
        <a href="/login">
          <label class="mt-3 text__checker" for="exampleCheck1"
            >Уже есть аккаунт - войдите!</label
          >
        </a>
      </div>
    </form>
  </div>
  <div class="lk">

  </div>
</template>

<script setup>
import { computed, reactive } from 'vue'
import axios from 'axios'


const Authorization = reactive({
  email: '',
  password: '',
  repeatpassword: '',
  username: ''
})

const submit = () => {
  console.log('submit');
  const pass1 = Authorization.password;
  const pass2 = Authorization.repeatpassword;
  if (pass1 !== pass2) {
    alert('Пароли должны совпадать!');
  } else {
    console.log(pass1);
    console.log(pass2);
    delete Authorization.repeatpassword;
    axios.post('http://127.0.0.1:8000/api/v1/auth/users/', Authorization)
      .then((response) => {
        console.log(response);
        alert('Вы успешно зарегистрировались!');
         
        // Перенаправление на страницу личного кабинета
        window.location.replace('/profil',);
      })
      .catch((error) => {
        console.log(error);
        alert('Произошла ошибка при регистрации!');
      });
  }
};

</script>



  
<style  scoped>

.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
} 

@media(max-width: 600){
      .body{
        justify-content: center;
        align-items: center;
      place-items: center;
      }
}



.button{
padding: 9px;
background-color: #CFC7F8;
width: 100%;
font-size: 1rem;
border-radius: 15px;
border: #CFC7F8;
color: black;
transition: all 0.2s ease-in-out;
}
.button:hover {
  cursor: pointer;
  opacity: 0.8;
  background-color:black;
  color:white
}


.title{
    text-align: center;
    font-size: 26px;
    font-weight: 700;
}
.text{
    text-align: center;

}



.authorization__form {
  max-width: 400px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  
  background-color: #F3F0FF;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0px 3px 6px rgb(0 0 0 / 10%);
  width: 400px;
}

.authorization__form .form-group {
  margin-bottom: 1rem;
}

.authorization__form label {
  font-weight: bold;
}

.authorization__form input[type="email"],
.authorization__form input[type="password"],
.authorization__form input[type="text"] {
  width: 100%;
  padding: 0.5rem;
  border-radius: 5px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

.authorization__form .button {
  display: block;
  margin: 0 auto;
  margin-top: 1rem;
}

.authorization__form .text__checker {
  color: #888;
}
.authorization__form .text__checker:hover {
  cursor: pointer;
  color: black;
}
</style>

  





  