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
  },

  /**
   * Retrieves a json object with the column names of both categorical and
   * numeric variables from the dataframe
   * @return {Object} The column names object.
   */
  getColumnNames() {
    return $axios.post(`data/column_names`, { sessionId: String(sessionStorage.sessionId) })
      .then(response => {
        return JSON.parse(response.data);
      })
  },

  /**
   * Retrieves the shape of the data (columns, rows)
   * @return {Object} The dataset shape.
   */
  getDataShape() {
    return $axios.post(`/data/shape`, { sessionId: String(sessionStorage.sessionId) })
      .then(response => {
        return JSON.parse(response.data);
      })
  }
}
