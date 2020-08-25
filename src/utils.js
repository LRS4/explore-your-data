/**
 * Retrieves column names from dataset.
 *
 * @param {Object} data
 * @return {Object} Object containing dataset rows.
 */
export const getDatasetColumns = (data) => {
  let columns = Object.keys(data);
  return columns.map(name => (
    {
      field: name,
      label: name
    }
  ));
}

/**
 * Transforms dataset into an object of row-data.
 *
 * @param {Object} data
 * @return {Object} Object containing dataset rows.
 */
export const getDatasetRows = (data) => {
  let rows = [];
  let numberOfRows = getRowCount(data);
  for (let i = 0; i < numberOfRows; i++) {
    let row = {};
    for (let col in data) {
      row[col] = data[col][i];
    }
    rows.push(row);
  }
  return rows;
}

/**
 * Counts the rows in each column and returns max count
 * 
 * @param {Object} data 
 * @return {Number} Count of rows
 */
export const getRowCount = (data) => {
  let rowsInColumns = []; 
  for (let col in data) {
    let rows = Object.keys(data[col]).length;
    rowsInColumns.push(rows);
  }
  return Math.max.apply(null, rowsInColumns);
}
