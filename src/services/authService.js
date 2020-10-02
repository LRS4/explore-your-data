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
  },

  /**
   * Determines the current environment and returns the relevant URI.
   * @return {String} The relevant URI for the current environment.
   */
  getEnvironmentURI() {
    let env = process.env.VUE_APP_ENV;
    if (env != null && env === "LocalDevelopment") {
      return process.env.VUE_APP_LOCALHOST_URI;
    } else {
      return process.env.VUE_APP_PROD_URI;
    }
  }
}
