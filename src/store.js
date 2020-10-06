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
      state.dataset = [dataset];
    },
    SET_METADATA(state, metadata) {
      state.metadata = metadata;
    }
  },
  // https://vuex.vuejs.org/guide/getters.html
  getters: {
    headColumns: state => {
      return getDatasetColumns(JSON.parse(state.dataset[0].dataset.head));
    },
    headRows: state => {
      return getDatasetRows(JSON.parse(state.dataset[0].dataset.head));
    }
  }
})
