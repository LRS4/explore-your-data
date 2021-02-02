import $axios from '../backend';

export default {
  /**
   * Uploads file to server.
   * @param {File} file The file to be uploaded.
   */
  uploadFile(file) {
    let formData = new FormData();
    formData.append('file', file);
    formData.set('sessionId', sessionStorage.sessionId);
    return $axios.post(`data/upload`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
      timeout: (60 * 1000) * 5
    })
      .then(res => {
        if (res.data === "Invalid data") {
          return res.data;
        } else {
          let dataset = JSON.parse(res.data);
          return dataset;
        }
      }).catch(err => {
        console.error(err);
      });
  }
}
