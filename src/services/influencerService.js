import $axios from '../backend';

export default {
  /**
  * Retrieves key influencers for the given column from the DataFrame
  * @return {Object} The key influencers json object.
  */
  getKeyInfluencers(analysisType, targetColumn, targetValue) {
    return $axios.post(`/data/influencers/${analysisType}/${targetColumn}/${targetValue}`, { sessionId: String(sessionStorage.sessionId) }, {
      timeout: (60 * 1000) * 3
    })
      .then(response => {
        return JSON.parse(response.data);
      })
  }
}
