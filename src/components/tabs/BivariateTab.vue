<template>
  <section>
    <div class="columns">
      <div class="column">
        <p class="is-size-5 mb-4">Select two variables</p>
        <div
          class="field"
          v-for="name in columnNames.numeric"
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
      </div>
      <div class="column is-four-fifths">
        <b-image
          v-bind:src="uri + 'api/plots/scatter-plot/' + timestamp + '/' + filename + '/' + x + '/' + y"
          placeholder="https://res.cloudinary.com/dayqxxsip/image/upload/l_text:Arial_34_bold:Loading visual...,g_north,y_240/e_brightness:60/e_grayscale,o_80/v1599306705/Analysis/pairplot_l4njly.png"
          webp-fallback=".jpg"
          v-if="showPlot"
        ></b-image>
      </div>
    </div>
  </section>
</template>

<script>
import authService from "../../services/authService";
import dataService from "../../services/dataService";

export default {
  name: "bivariate",
  data() {
    return {
      filename: sessionStorage["sessionId"],
      timestamp: Date.now(),
      uri: authService.getEnvironmentURI(),
      checkboxGroup: [],
      columnNames: [],
      showPlot: false,
      x: null,
      y: null,
      hue: "none"
    };
  },
  created() {
    this.getColumnNames();
  },
  methods: {
    async getColumnNames() {
      this.columnNames = await dataService.getColumnNames();
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
