<template>
  <section class="image-container">
    <b-image
      v-bind:src="uri + 'api/plots/correlation/' + timestamp + '/' + filename"
      placeholder="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png"
      webp-fallback=".jpg"
      ratio="16by9"
    >
    </b-image>
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
