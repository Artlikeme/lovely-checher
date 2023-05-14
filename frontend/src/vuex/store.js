import {createStore} from 'vuex'
import axios from 'axios';
import { reactive } from 'vue';
const store=createStore({
  state:{
    backendUrl: "http://127.0.0.1:8000/api/v1",
    top_3_products:[],
    news:[],
    hotels:[],
    rests:[],
    theaters:[],
    parks:[],
    last_viewed:[],
    favourites:[],
    
    isLoggedIn: false,



    
  },
  


 

  mutations:{
    setLoggedIn(state, value) {
      state.isLoggedIn = value;
    },
    SET_FAVOURITES_TO_STATE:(state,favourites)=>{
      state.favourites=favourites;
     
       },
     

    SET_LAST_VIEWED_TO_STATE:(state,last_viewed)=>{
      state.last_viewed=last_viewed;
     
       },
    SET_TOP_3_PRODUCTS_TO_STATE:(state,top_3_products)=>{
   state.top_3_products=top_3_products;
  
    },
    SET_NEW_TO_STATE:(state,news)=>{
      state.news=news;
     
       },
    
    SET_CARD_HOTEL_PRODUCTS_TO_STATE:(state,hotels)=>{
    state.hotels=hotels;
    },
    SET_CARD_THEATER_PRODUCTS_TO_STATE:(state,theaters)=>{
      state.theaters=theaters;
    },
    SET_CARD_REST_PRODUCTS_TO_STATE:(state,rests)=>{
      state.rests=rests;
    },
    SET_CARD_PARK_PRODUCTS_TO_STATE:(state,parks)=>{
      state.parks=parks;
    },
  },







  actions:{
    
    submit({ commit }, Login) {
     
      if (response.status === 200) {
        commit('setLoggedIn', true);
    
      }
   
    },
    async GET_FAVOURITES_FROM_API({commit}){
      try {
        const favourites= await axios("http://127.0.0.1:8000/api/v1/item/topthree	", {
          method: "GET"
        });
        commit('SET_FAVOURITES_TO_STATE', favourites.data);
        return favourites;
      }
       catch (error) {
        console.log(error);
        return error;
      }
    }, 






    async GET_LAST_VIEWED_FROM_API({commit}){
      try {
        const last_viewed = await axios("http://127.0.0.1:8000/api/v1/item/lastthree	", {
          method: "GET"
        });
        commit('SET_LAST_VIEWED_TO_STATE', last_viewed.data);
        return last_viewed;
      }
       catch (error) {
        console.log(error);
        return error;
      }
    }, 






    async GET_PRODUCTS_FROM_API({commit}) {
      try {
          const top_3_products = await axios("http://127.0.0.1:8000/api/v1/item/topthree", {
              method: "GET",
          });
          commit('SET_TOP_3_PRODUCTS_TO_STATE', top_3_products.data);
          console.log(top_3_products)
          return top_3_products;
      } catch (error) {
          return error;
      }
  },
    async GET_PRODUCTS_HOTEL_FROM_API({commit}) {
      try {
          const hotels = await axios("http://127.0.0.1:8000/api/v1/item/list?search=Hotel", {
              method: "GET"
          });
          console.log(hotels)
          commit('SET_CARD_HOTEL_PRODUCTS_TO_STATE', hotels.data.results);
          return hotels;
      } catch (error) {
          return error;
      }
  },
    
    async GET_PRODUCTS_NEW_FROM_API({commit}){
      try {
        const news = await axios("http://127.0.0.1:8000/api/v1/news/1", {
          method: "GET"
        });
        commit('SET_NEW_TO_STATE', news.data);
        return news;
      }
       catch (error) {
        
        return error;
      }
    },



 

  async GET_PRODUCTS_THEATER_FROM_API({commit}){
    try{
    const theaters = await axios (" http://127.0.0.1:8000/api/v1/item/list?search=Theatre/Cinema",{
      method:"GET"
    });
    commit('SET_CARD_THEATER_PRODUCTS_TO_STATE',theaters.data.results);
    return theaters;
  }
  catch (error){
    console.log(error);
    return error;
  }
},


async GET_PRODUCTS_REST_FROM_API({commit}){
  try{
  const rests = await axios (" http://127.0.0.1:8000/api/v1/item/list?search=Cafe/Restaurant ",{
    method:"GET"
  });
  commit('SET_CARD_REST_PRODUCTS_TO_STATE',rests.data.results);
  return rests;
}
catch (error){
  console.log(error);
  return error;
}
},

async GET_PRODUCTS_PARK_FROM_API({commit}){
  try{
  const parks = await axios (" http://127.0.0.1:8000/api/v1/item/list?search=Parks/Squares",{
    method:"GET"
  });
  commit('SET_CARD_PARK_PRODUCTS_TO_STATE',parks.data.results);
  return parks;
}
catch (error){
  console.log(error);
  return error;
}
},






  },







  getters:{
    TOP_3_PRODUCTS(state){
      return state.top_3_products;
    },
    
      getIsLoggedIn(state) {
        return state.isLoggedIn;
      },
    NEWS(state){
      return state.news;
    },
  HOTELS(state){
       return state.hotels;
  },
  THEATERS(state){
    return state.theaters;
},
  RESTS(state){
  return state.rests;
},
PARKS(state){
  return state.parks;
},
LAST_VIEWED(state){
  return state.last_viewed;
},
FAVOURITES(state){
  return state.favourites;
},


  }


})
export default store;