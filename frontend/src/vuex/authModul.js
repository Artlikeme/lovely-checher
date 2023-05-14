// auth.js

const state = {
  isLoggedIn: false
}

const mutations = {
  setLoggedIn(state, value) {
    state.isLoggedIn = value
  }
}

export default {
  namespaced: true,
  state,
  mutations
}