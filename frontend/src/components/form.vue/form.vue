<script setup lang='ts'>
import { computed, reactive } from 'vue'
import axios from 'axios'

const object = reactive({
  city: '',
  category: '',
  fio: '',
  title: '',
  address: '',
  telephone: '',
  opening_hours: '',
  date_of_foundation: '',
  prace: '',
  parking: '',
  price_list_for_hotels:'',
})

// Поля для каждой категории объектов (ключи соответствуют значениям из селекта)
const fieldsByCategory = {
  // Развлечения:
  'Театры/Кинотеатры': ['address', 'opening_hours', 'date_of_foundation', 'telephone'],
  // Природа:
  'Парки/Скверы': ['address', 'opening_hours', 'date_of_foundation', 'telephone'],
  // Кафе / Рестораны:
  'Кафе/Рестораны': ['address', 'opening_hours', 'telephone', 'prace', ' parking'],
  // Отели:
  'Отели': ['address', 'opening_hours', 'telephone', 'price_list_for_hotels', ' parking'],
}

// Вычисляемое свойство, возвращающее поля для текущей категории
const categoryFields = computed(() => {
  const fields = fieldsByCategory[object.category]
  return Array.isArray(fields) ? fields : []
})

// Функция отправки формы
const submitForm = () => {
  console.log('submit');
  axios.post('/', object).then((response) => {
    console.log(response)
  }).catch((error) => {
    console.log(error)
  })
}

</script>


<template>
  <div class="wrapper">
    <form class="form1" @submit.prevent.stop="submitForm">
  
        <!-- Заголовок -->
  <div class="title">Форма добавления объекта</div>

  <!-- Выбор города -->
  <div class="form-group">
    <label for="city">Выберите город:</label>
    <select name="city" id="city" v-model="object.city" required>
      <option value="">--Выберите город--</option>
      <option value="Таганрог">Таганрог</option>
      <option value="Астрахань">Астрахань</option>
      <option value="Москва">Москва</option>
    </select>
  </div>

  <!-- Выбор категории -->
  <div class="form-group">
    <label for="category">Выберите категорию объекта:</label>
    <select name="category" id="category" v-model="object.category" required>
      <option value="">--Выберите категорию--</option>
      <option value="Театры/Кинотеатры">Театры/Кинотеатры</option>
      <option value="Парки/Скверы">Парки/Скверы</option>
      <option value="Кафе/Рестораны">Кафе/Рестораны</option>
      <option value="Отели">Отели</option>
    </select>
  </div>
  
       <!-- Поля для каждой категории объектов -->
<div v-if="categoryFields.length > 0">
  <div v-for="(field, index) in categoryFields" :key="'field-'+index" class="form-group">
    <!-- Название поля в зависимости от выбранной категории -->
    <label>{{ field }}:</label>
    <!-- Ввод данных пользователя в поле формы -->
    <input type="text" v-model="object[field]" placeholder="" required/>
  </div>
</div>

<!-- Имя пользователя -->
<div class="form-group">
  <label for="author">Имя пользователя:</label>
  <input type="text" id="author" v-model="object.fio" placeholder="" required/>
</div>

<!-- Название объекта -->
<div class="form-group">
  <label for="title">Название объекта:</label>
  <input type="text" id="title" v-model="object.title" placeholder="" required/>
</div>

<!-- Кнопка отправки формы -->
<button type="submit" class="button2">Добавить</button>

</form>
</div>
  
</template>




<style >

.form-group{
  display: flex;
  flex-direction: column;
  width: 100%;
}
.button2{
  margin-top: 70px;
  width: 421px;
  height: 38px;
  border-radius: 0.375rem;
  border: 2px solid #CFC7F8;
  background-color: #E3DDFF;

}



.form1{
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #F3F0FF;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0px 3px 6px rgb(0 0 0 / 10%);
  width: 400px;
  margin: 0 auto;
}

#exampleInputrea{
  margin-top: 20px;
    border-radius: 0.375rem;
    border: 2px solid #CFC7F8;
    width: 421px;
    height: 100px;
}





#exampleInput{
    margin-top: 20px;
    border-radius: 0.375rem;

    height:37.6px;
    border: 2px solid #CFC7F8;
}

#object-select{
    margin: 10px 0px;
    width: 100%;
    height: 37.6px;
    border-radius: 0.375rem;
    border: 1px solid #ced4da;
}

</style>