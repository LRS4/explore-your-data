import $axios from '../backend';

export default {
  async fetchLinks() {
    return $axios.get(`resource/get-useful-links`)
      .then(response => response.data)
  }
}
