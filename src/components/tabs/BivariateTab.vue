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
        <p class="is-size-5 mb-4">Select hue (optional)</p>
      </div>
      <div class="column is-four-fifths">
        <b-image
          v-bind:src="uri + 'api/plots/scatter-plot/' + timestamp + '/' + filename + '/' + x + '/' + y"
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
