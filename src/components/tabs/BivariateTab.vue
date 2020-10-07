<template>
  <section>
    <div class="columns">
      <div class="column" v-if="metadata">
        <p class="is-size-5 mb-4">Select two variables</p>
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
        <p 
          v-if="categoricalDescriptions.Name" 
          class="is-size-5 mb-4">
          Select hue (optional)
        </p>
        <div
          class="field"
          v-for="(property, name) in categoricalDescriptions"
          v-bind:key="name.id"
        >
          <b-radio 
            v-if="property.unique < 20"
            v-model="hue"
            type="is-info"
            name="name"
            :native-value="name">
            {{ name }}
            </b-radio>
        </div>
        <p class="is-size-5 mb-4">Options</p>
        <div
          class="field"
        >
          <b-checkbox
            v-model="showRegressionLine"
            type="is-info"
            :native-value="1"
          >
            Regression plot
          </b-checkbox>
        </div>
      </div>
      <div class="column is-four-fifths">
        <b-image
          v-bind:src="uri + 'api/plots/scatter-plot/' + timestamp + '/' + filename + '/' + x + '/' + y + '/' + hue + '/' + reg"
          placeholder="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png"
          webp-fallback=".jpg"
          ratio="15by11"
          v-if="showPlot"
        >
        </b-image>
      </div>
    </div>
  </section>
</template>

<script>
import authService from "../../services/authService";

export default {
  name: "bivariate",
  data() {
    return {
      filename: sessionStorage["sessionId"],
      timestamp: Date.now(),
      uri: authService.getEnvironmentURI(),
      checkboxGroup: [],
      showRegressionLine: [], 
      columnNames: [],
      showPlot: false,
      x: null,
      y: null,
      hue: 'none',
      reg: 0
    };
  },
  computed: {
    metadata() {
      return this.$store.state.metadata.metadata;
    },
    categoricalDescriptions() {
      return JSON.parse(this.$store.state.dataset[0].dataset.cat_describe);
    }
  },
  watch: {
    checkboxGroup(arr) {
      if (arr.length === 2) {
        console.log("Two variables selected!", arr);
        this.x = this.checkboxGroup[0];
        this.y = this.checkboxGroup[1];
        this.showPlot = true;
      } else {
        this.x = null;
        this.y = null;
        this.showPlot = false;
      }
    },
    showRegressionLine(arr) {
      if (this.checkboxGroup.length === 2) {
        if (arr.length > 0) {
          this.reg = 1;
        } else {
          this.reg = 0;
        }
      }
    }
  }
};
</script>
