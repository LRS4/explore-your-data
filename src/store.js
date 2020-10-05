import Vue from 'vue'
import Vuex from 'vuex'
import { getDatasetColumns, getDatasetRows } from './utils'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    dataset: [],
    metadata: {}
  },
  actions: {
    setDataset({ commit }, dataset) {
      commit('SET_DATASET', dataset);
    },
    setMetaData({ commit }, metadata) {
      commit('SET_METADATA', metadata);
    }
  },
  mutations: {
    SET_DATASET(state, dataset) {
      state.dataset = [dataset]
    },
    SET_METADATA(state, metadata) {
      state.metadata = metadata
    }
  },
  // https://vuex.vuejs.org/guide/getters.html
  getters: {
    columns: state => {
      return getDatasetColumns(state.dataset[0].dataset);
    },
    rows: state => {
      return getDatasetRows(state.dataset[0].dataset);
    }
  }
})
