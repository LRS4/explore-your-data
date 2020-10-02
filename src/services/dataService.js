import $axios from '../backend';

export default {
  /**
   * Retrieves a description of the numeric variables in the dataset
   * from the pandas describe method
   * @return {Object} The dataset description object.
   */
  getNumericVariablesSummary() {
    return $axios.post(`data/describe/numeric`, { sessionId: String(sessionStorage.sessionId) })
      .then(response => {
        return JSON.parse(response.data);
      })
  },

  /**
   * Retrieves a description of the categorical variables in the dataset
   * from the pandas describe method
   * @return {Object} The dataset description object.
   */
  getCategoricalVariablesSummary() {
    return $axios.post(`data/describe/categorical`, { sessionId: String(sessionStorage.sessionId) })
      .then(response => {
        return JSON.parse(response.data);
      })
  }
}
