<template>
  <div class="wrapper">
    <h1>Отправить отзыв</h1>
    <div class="comments">
      <div class="name">
        <label>Имя пользователя:</label>
        <div>{{  object.name }}</div>
      </div>
    
     
      <div class="photo">
        <label>Фото:</label>
        <input  type="file" ref="fileInput" @change="handleFileUpload()" accept="image/*">
      </div>
      <div class="rating">
        <label for="rating-select">Оценка:</label>
        <select id="rating-select" v-model=" object.rating">
          <option value="1">Ужасно</option>
          <option value="2">Плохо</option>
          <option value="3">Нормально</option>
          <option value="4">Хорошо</option>
          <option value="5">Отлично</option>
        </select>
      </div>
      <div class="user_comment">
        <label>Комментарий:</label>
        <textarea v-model=" object.description"></textarea>
      </div>
      <div class="btn_comment">
        <button @click.prevent="submitReview()">Отправить</button>
      </div>
    </div>
    <div v-if=" objects.length">
      <h2>Отзывы:</h2>
      <div class="wrapper_comment" v-for=" object in  objects" :key=" object.id">
        <div class="comment_user_name">{{  object.name }} </div>
        
        <div   class="comment_user_photo" v-if=" object.photo">
          <img :src=" object.photo" alt="Отзыв"/>
        </div>
        <div class="comment_user_rating">Оценка: {{  object.rating }}</div>
        <div class="comment">Комментарий: 
          
          <textarea id="comment" name="comment" readonly="True">{{  object.description }}</textarea>
          
        </div>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>



export default {
  
  components: {
    
  },
  props: {
        objects: {
            type: Object
        },
        
      },
  data() {
    return {
      object: {
       name:'Алексей Михайлов',
     
        photo: null,
        rating: 3,
        description: '',
      },
      // objects: [],
    };
  },
  mounted() {
    this.loadUserReview();
    this.loadReviews();
  },
  methods: {
    loadUserReview() {
      // Получить данные пользователя из JSON файла и обновить review объект
    },
    handleFileUpload() {
      const file = this.$refs.fileInput.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        this.object.photo = reader.result;
      };
    },
    submitReview() {
      // Отправка отзыва на сервер
      // Обновить review объект
      // Добавить отправленный отзыв в список отзывов
      this.objects.push({ ...this.object});
      // Сбросить поле выбора файла и объекта review.photo
      this.$refs.fileInput.value = '';
      this.object.photo = null;
      // Очистить review объект
      document.getElementById("comment").disabled = true; // Запретить редактирование текста в textarea
      this.object = {
       
        photo: null,
        rating:"1",
        description: '',
      };
    },
    loadReviews() {
      // Получить список отзывов и обновить reviews массив

      const url = '';
  fetch(url)
    .then(response => response.json())
    .then(data => {
      this. objects = data;
    })
    .catch(error => {
      // Обрабатываем ошибку
      console.error('Error loading reviews:', error);
    });
    },
  },
};
</script>

<style>
#comment {
  width:800px;
  height: 300px;
  min-height: 50px; /* минимальная высота поля */
  padding:10px;
  resize: none;
  border-radius: 20px;
   /* Стиль границы и фона */
  margin: 0 auto;
   border :1px solid #ccc;

    /* Разрешаем перенос слов */
    word-wrap :break-word;

}
.comment{
  padding: 30px 0px 30px 30px;
}

.comment_user_name{
padding: 30px 0px 30px 10px
}
.wrapper_comment{
  width: 960px;
  
  background-color: #E3DDFF;
  border-radius: 20px;
  
}

.comment_user_photo{
  width: 780px;
  height: 400px;
 
  margin: 0 auto;
  border: 5px solid black;

}
.comment_user_photo img{
  object-fit: cover;
  width: 100%;
  height: 100%;
 
}
.comment_user_description{
 margin: 0 auto;
  width: 780px;
  word-wrap: break-word;
}
.comment_user_rating{
  padding: 30px 0px 0px 30px;
}
.user_comm{
 padding-right: 30px;
}
#rating-select{
  background-color: white;
    outline: none;
    border: none;
    height: 30px;
    border-radius: 10px;
   
}



.wrapper {
  max-width: 960px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  color: #333;
}

h1 {
  font-size: 32px;
  margin-bottom: 20px;
}

.comments {
  
  
  background-color: #CFC7F8;
  display: flex;
  flex-wrap: wrap;
height: 360px;
margin: 0 auto;
border-radius: 10px;
padding: 30px;
}

.comments > div {
  margin-bottom: 10px;
  flex-basis: 50%;
}

.comments label {
  display: inline-block;
  width: 120px;
  margin-right: 10px;
  font-weight: bold;
}

.comments input[type="file"] {
  margin-top: 10px;
}

.comments textarea {
  height: 137px;
  width: 900px;
  padding: 10px;
  resize: vertical;
  border-radius: 20px;

  resize: none; /* Запрещаем изменять размер */
}

.comments button {
  background-color: #4346A1;
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 30px;
}

.comments button:hover {
  background-color: black;
  color: white;
}

h2 {
  font-size: 24px;
  margin-top: 40px;
  margin-bottom: 20px;
}

img {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
 
}

hr {
  border: none;
  border-top: 1px solid #ddd;
  margin-top: 20px;
}

.photo input{
  background-color:#CFC7F8;
  border: none;
  
}


</style>