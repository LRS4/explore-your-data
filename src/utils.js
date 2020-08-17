export const getDatasetColumns = (data) => {
  let columns = Object.keys(data);
  return columns.map(name => (
    {
      field: name,
      label: name
    }
  ));
}

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

export const getRowCount = (data) => {
  let rowsInColumns = []; 
  for (let col in data) {
    let rows = Object.keys(data[col]).length;
    rowsInColumns.push(rows);
  }
  return Math.max.apply(null, rowsInColumns);
}
