import Vue from 'vue'
import Vuex from 'vuex'
import { getDatasetColumns, getDatasetRows } from './utils'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    metadata: {},
    images: {
      'missingDataImg': null
    }
  },
  actions: {
    setMetadata({ commit }, metadata) {
      commit('SET_METADATA', metadata.metadata);
    },
    cacheImage({ commit }, payload) {
      commit('CACHE_IMAGE', payload);
    }
  },
  mutations: {
    SET_METADATA(state, metadata) {
      state.metadata = metadata;
    },
    CACHE_IMAGE(state, payload) {
      state.images[payload.name] = payload.img;
    }
  },
  // https://vuex.vuejs.org/guide/getters.html
  getters: {
    headColumns: state => {
      if (Object.keys(state.metadata).length > 0) {
        return getDatasetColumns(JSON.parse(state.metadata.head));
      }
    },
    headRows: state => {
      if (Object.keys(state.metadata).length > 0) {
        return getDatasetRows(JSON.parse(state.metadata.head));
      }
    },
    tailColumns: state => {
      if (Object.keys(state.metadata).length > 0) {
        return getDatasetColumns(JSON.parse(state.metadata.tail));
      }
    },
    tailRows: state => {
      if (Object.keys(state.metadata).length > 0) {
        return getDatasetRows(JSON.parse(state.metadata.tail));
      }
    }
  }
})
