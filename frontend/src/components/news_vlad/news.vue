<script setup>
import { computed, reactive, } from 'vue'
import axios from 'axios'

const news = reactive({
    number: '',
    photo: null,
    title: '',
    discription: '',
})
const previewFilePath = computed(() =>{
    if(news.photo){
        return URL.createObjectURL(news.photo) 
    }
    return'#'
   
})
const uploadFile=(e) =>{
    const file = e.target.files[0];
    news.photo = file;
}
const submit = () => {
    alert("Новость отправлена")
  console.log('submit');
  axios.post('/',news).then((response) =>{
    console.log(response)

  }).catch((error) =>{
    console.log(error)
  })
}

</script>
<template>
<div class="wrapper">
    
        <form 
        @submit.prevent.stop = "submit"
        >
        <div class="plus">
        <div class="plus__wrapper">
        <div class="plus__title">Опубликовать новость:</div>
        <div class="plus__list">
            <select class = "plus_item" name="object" id="object"
            v-model="news.number"
>
    <option value="">Выбрать объект</option>
    <option value="Объект 1">Объект 1</option>
    <option value="Объект 2">Объект 2</option>
    <option value="Объект 3">Объект 3</option>

  </select>
        </div>
        <div class="new">
            <div class="new__alt">
                <input 
                @change="uploadFile"
                type="file" class="form-control-file" id="exampleFormControlFile1">
                
</div>
<p class="photo__center">Добавить фото</p>
<div class="preview">
    
</div>


</div>
<div v-if="news.photo" class="if">

<img class="preview__photo" :src="previewFilePath" alt="">
</div>

<input 
v-model="news.title"
 type="text" class="form-control" id="exampleInput" placeholder="Введите заголовок">
<div class="textarea">
<textarea 
v-model="news.discription"
 class=" form-control12" id="exampleInputarea" rows="3" placeholder="Добавить текст..."></textarea>
</div>

<button type="submit" class="button_news_vlad" id="btnformvlad">Добавить</button>

</div>
</div>

</form>
    
</div>

</template>

<style >







.plus{
width: 100%;
background: #CFC7F8;
border-radius: 20px;
}

.plus__wrapper{
   
    padding: 40px;
}

.plus__title{
    padding-top: 11px;
    padding-left: 2px;
font-size: 18px;

line-height: 22px;
letter-spacing: 0em;
padding-bottom: 30px;


    
}
.plus_item{
    
    width: 100%;
    height: 39.2px;
    border-radius: 20px;
}
.plus__list{
    
    border-radius: 20px;
    border: 2px solid white;
    width: 211px;
    margin-bottom: 20px;
}

.new{
    

height: 350px;
width:800px;
margin: 0px auto;
background-color: white;
border-radius: 20px;
position: relative;
padding: 145px 0px;


}

.new__alt{
display: flex;
    --b: 4px; /* the thickness */
  width: 60px; /* the size */
  aspect-ratio: 1;
  border: 10px solid #ffffff; /* the outer space */
  background: conic-gradient(from 90deg at var(--b) var(--b),
  #fff 90deg,#000 0) calc(100% + var(--b)/2) 
  calc(100% + var(--b)/2)/ calc(50% + var(--b)) calc(50% + var(--b));

  justify-content: center;
  align-items: center;
  text-align: center;
margin: 0px auto;
cursor: pointer;


}

.photo__center{
    text-align: center;
    font-size: 16px;
line-height: 19px;
padding-top: 20px;
}
.form-control-file{
    opacity: 0%;
    width: 60px;
    
}

.other{
    width: 200px;
    margin: 0 auto;
}
#exampleInputarea{
    width: 911px;
    height: 181px;
    margin-top: 20px;
    
    border-radius: 0.375rem;
    border: 2px solid #CFC7F8;
}

.textarea{
    width: 918px;
    height: 181px;
}

#exampleInput{
    margin-top: 20px;
    border-radius: 0.375rem;
   
    height:37.6px;
    border: 2px solid #CFC7F8;
}

.preview__photo{
    margin-top: 10px;
    width: 125px;
    height: 125px;
}
.button_news_vlad{

  padding: 9px;
  background-color: #CFC7F8;
  width: 15%;
  font-size: 1rem;
  border-radius: 15px;
  border: #CFC7F8;
  color: black;
  font-weight: 600;
  transition: all 0.2s ease-in-out;

  }
  .button_news_vlad:hover {
    cursor: pointer;
    opacity: 0.8;
    background-color:black;
    color:white
  }



</style>




