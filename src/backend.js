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

  uploadFile (file) {
    let formData = new FormData();
    formData.append('file', file);
    return $axios.post(`data/upload`, formData, { timeout: 10000 })
      .then(res => {
        let data = JSON.parse(res.data);
        console.log(data);
      }).catch(err => {
        console.error({ err });
      });
  }
}
