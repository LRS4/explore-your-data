<template>
  <section>
    <div class="columns is-gapless" style="height: 10px;">
      <div class="column">
        <span class="tag is-info mr-2">{{ totalMissingValues }} missing values</span>
        <span class="tag is-info">{{ totalMissingPercent }}% missing</span>
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
    :src="missingDataImg.src"
    placeholder="https://res.cloudinary.com/dayqxxsip/image/upload/v1603883887/Shared/placeholder-image_ccgbjr.png"
    webp-fallback=".jpg"
    ratio="16by9"
    class="mt-5"
    rel="preload"
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
  },
  computed: {
    missingDataImg() {
      if (
        this.$store.state.missingDataImg !== null || 
        this.$store.state.missingDataImg !== undefined
      ) {
        return this.$store.state.images.missingDataImg;
      }
    },
    totalMissingPercent() {
      if (Object.keys(this.$store.state.metadata).length > 0) {
        return this.$store.state.metadata.totalMissingPercent;
      }
    },
    totalMissingValues() {
      if (Object.keys(this.$store.state.metadata).length > 0) {
        return this.$store.state.metadata.totalMissingValues;
      }
    }
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
