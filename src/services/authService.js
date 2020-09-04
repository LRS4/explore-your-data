import $axios from '../backend';

export default {
  /**
   * Retrieves a unique session ID and sets in session storage.
   * @return {Boolean} True or false indicating success or failure.
   */
  getUniqueSessionId() {
    return $axios.post(`session/create`)
      .then(response => {
        sessionStorage['sessionId'] = response.data;
        console.log("Session token set.");
      })
  }
}
