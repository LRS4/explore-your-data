import $axios from '../backend';

export default {
  /**
   * Retrieves an description of the dataset from pandas describe method
   * @return {Object} The dataset description object.
   */
  getDataSummary() {
    return $axios.post(`data/describe`, { sessionId: String(sessionStorage.sessionId) })
      .then(response => {
        console.log("data", response.data);
        return JSON.parse(response.data);
      })
  }
}
