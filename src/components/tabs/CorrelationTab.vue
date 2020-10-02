<template>
  <section>
    <b-image
      v-bind:src="uri + 'api/plots/correlation/' + timestamp + '/' + filename"
      placeholder="https://res.cloudinary.com/dayqxxsip/image/upload/l_text:Arial_34_bold:Loading visual...,g_north,y_240/e_brightness:60/e_grayscale,o_80/v1599306705/Analysis/pairplot_l4njly.png"
      webp-fallback=".jpg"
    ></b-image>
  </section>
</template>

<script>
import authService from '../../services/authService';

export default {
  name: "correlation",
  data() {
    return {
      filename: sessionStorage["sessionId"],
      timestamp: Date.now(),
      uri: authService.getEnvironmentURI()
    };
  }
};
</script>

<style>
.image img {
  height: 80%;
  width: 80%;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
