import axios from 'axios'

let $axios = axios.create({
  baseURL: '/api/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Request Interceptor
$axios.interceptors.request.use(function (config) {
  config.headers['Authorization'] = 'Fake Token'
  return config
})

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // Handle Error
  console.log(error)
  return Promise.reject(error)
})

export default {

  fetchResource () {
    return $axios.get(`resource/xxx`)
      .then(response => response.data)
  },

  fetchSecureResource () {
    return $axios.get(`secure-resource/zzz`)
      .then(response => response.data)
  },

  fetchLinks () {
    return $axios.get(`resource/get-useful-links`)
      .then(response => response.data)
  },
 
  /**
   * Uploads file to server.
   * @param {File} file The file to be uploaded.
   */
  uploadFile (file) {
    let formData = new FormData();
    formData.append('file', file);
    return $axios.post(`data/upload`, formData, { timeout: 60000 })
      .then(res => {
        if (res.data === "Invalid data") {
          return res.data;
        } else {
          let dataset = JSON.parse(res.data);  
          return dataset;
        }
      }).catch(err => {
        console.error({ err });
      });
  }
}
