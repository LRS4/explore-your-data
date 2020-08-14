import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    dataset: []
  },
  actions: {
    setDataset({ commit }, dataset) {
      commit('SET_DATASET', dataset);
    }
  },
  mutations: {
    SET_DATASET(state, dataset) {
      state.dataset = [dataset]
    }
  }
})
