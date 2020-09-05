<template>
  <section>
    <b-image
      v-bind:src="'http://localhost:8080/api/plots/pairplot/' + timestamp + '/' + filename"
      placeholder="https://res.cloudinary.com/dayqxxsip/image/upload/l_text:Arial_34_bold:Loading visual...,g_north,y_240/e_brightness:60/e_grayscale,o_80/v1599306705/Analysis/pairplot_l4njly.png"
      webp-fallback=".jpg"
      ratio="1by1"
    ></b-image>
  </section>
</template>

<script>
export default {
  name: "bivariate",
  data() {
    return {
      filename: sessionStorage["sessionId"],
      timestamp: Date.now(),
    };
  }
};
</script>
