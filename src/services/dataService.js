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
  },

  /**
   * Retrieves information / metadata on the DataFrame
   * @return {Object} The metadata json object.
   */
  getMetaData() {
    return $axios.post(`/data/metadata`, { sessionId: String(sessionStorage.sessionId) }, {
      timeout: (60 * 1000) * 2
    })
      .then(response => {
        return JSON.parse(response.data);
      })
  },

  /**
   * Retrieves unique values for the given column from the DataFrame
   * Populates the unique values for the key influencers categorical dropdown
   * @return {Object} The unique values json object.
   */
  getUniqueValues(column) {
    return $axios.post(`/data/uniques/${column}`, { sessionId: String(sessionStorage.sessionId) })
      .then(response => {
        return JSON.parse(response.data);
      })
  },

  /**
   * Retrieves a crosstab/pivot table DataFrame for two variables
   * @param {String} x The x axis variable name 
   * @param {String} y The y axis variable name
   * @return {Object} The crosstab DataFrame as a json object.
   */
  getCrosstab(x, y, showPercentages) {
    return $axios.post(`/data/crosstab/${x}/${y}/${showPercentages}`, { sessionId: String(sessionStorage.sessionId) })
      .then(response => {
        return response.data;
      })
  }
}
