<template>
  <div class="wrapper" :isLoggedIn="isLoggedIn">
    <form @submit.prevent.stop="submit" >
      <div class="title">Вход</div>
      <div class="form-group">
        <label for="exampleInputEmail2">Email</label>
        <input
          v-model="Login.username"
          type=""
          class="mt-2 form-control"
          id="exampleInputEmail2"
          aria-describedby="emailHelp"
          placeholder="example@email.com"
        />
      </div>
      <div class="form-group">
        <label for="exampleInputPassword2">Пароль</label>
        <input
          v-model="Login.password"
          type="password"
          class="mt-2 mb-2 form-control"
          id="exampleInputPassword2"
          placeholder="******"
        />
      </div>
      
       <button   type="submit" class="button">Войти</button>
       
      <div class="text">
        <a href="/authorizarion">
          <label class="mt-3 text__checker" for="exampleCheck2">Еще не зарегистрированы?</label>
        </a>
      </div>
      <div v-if="data.isLoggedIn">Вы успешно вошли!</div>
      <div v-else >Зарегистрируйтесь!У вас появиться личный кабинет с большм функционалом!</div>
    </form>

  </div>
</template>

<script setup>
// В вашем компоненте
import store from "../../vuex/store";
import { reactive } from "vue";
import axios from "axios";

const Login = reactive({
  username: "",
  password: "",
});

const submit = () => {
  console.log("submit");
  axios
    .post("http://127.0.0.1:8000/api/v1/auth/token/login", Login)
    .then((response) => {
      console.log(Login)
      console.log(response);
      // Проверяем, успешно ли выполнен вход и устанавливаем соответствующее значение переменной состояния
      if (response.status === 200) {
        // Сохраняем данные пользователя в store
        store.commit("setLoggedIn", true);
        // Сохраняем токен доступа в localStorage или cookie
        localStorage.setItem("token", response.data.token);
        // Перенаправляем пользователя на страницу профиля
        window.location.replace('/profil');
      }
      
    })
    .catch((error) => {
      console.log(error);
    });
};
</script>

<style scoped > 
.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
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