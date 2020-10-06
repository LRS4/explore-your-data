<template>
  <section>
    <div class="columns">
      <div class="column" v-if="metadata">
        <p class="is-size-5 mb-4">Select variables</p>
        <div
          class="field"
          v-for="name in metadata.columnsInfo.num_col_names"
          v-bind:key="name.id"
        >
          <b-checkbox
            v-model="checkboxGroup"
            type="is-info"
            :native-value="name"
          >
            {{ name }}
          </b-checkbox>
        </div>
        <b-button class="button-secondary is-light is-medium" @click="updateCorrPlot()">
          <span>Update</span>
        </b-button>
        <br />
      </div>
      <div class="column is-four-fifths">
        <b-image
          v-if="showImage"
          v-bind:src="uri + 'api/plots/correlation/' + timestamp + '/' + filename + '/' + selectedColumns"
          placeholder="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png"
          webp-fallback=".jpg"
          ratio="16by10"
        >
        </b-image>
      </div>
    </div>
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
      uri: authService.getEnvironmentURI(),
      checkboxGroup: [],
      selectedColumns: null,
      showImage: false
    };
  },
  methods: {
    updateCorrPlot() {
      if (this.checkboxGroup.length >= 2) {
        console.log(this.checkboxGroup);
        this.selectedColumns = this.checkboxGroup.join();
        this.showImage = true;
      } else {
        this.selectedColumns = null;
        this.showImage = false;
      }
    }
  },
  computed: {
    metadata() {
      return this.$store.state.metadata.metadata;
    },
    numericalDescriptions() {
      return JSON.parse(this.$store.state.dataset[0].dataset.num_describe);
    },
    isLowColumnCount() {
      let cols = JSON.parse(this.$store.state.dataset[0].dataset.num_describe);
      return Object.keys(cols).length <= 7;
    }
  },
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
