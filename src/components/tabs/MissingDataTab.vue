<template>
  <section>
    <div class="columns is-gapless" style="height: 10px;">
      <div class="column">
      </div>
      <div class="column">
        <a 
          v-bind:href="uri + 'api/data/impute-missing-data/' + timestamp + '/' + filename"
          class="link is-pulled-right" 
          target="_blank">
          Fill missing data <b-icon icon="download" size="is-small"></b-icon>
        </a>
      </div>
    </div>
    <b-image
      v-bind:src="uri + 'api/plots/missing-data-plot/' + timestamp + '/' + filename"
      placeholder="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png"
      webp-fallback=".jpg"
      ratio="16by9"
      class="mt-5"
    >
    </b-image>
  </section>
</template>

<script>
import authService from '../../services/authService';

export default {
  name: "missing",
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
