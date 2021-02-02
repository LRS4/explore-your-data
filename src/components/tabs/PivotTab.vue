<template>
  <section>
    <div class="columns">
      <div class="column" v-if="nunique">
        <p class="is-size-5 mb-4">Select two variables</p>
        <div
          class="field"
          v-for="(value, name) in nunique"
          v-bind:key="name.id"
        >
          <b-checkbox
            v-if="value < 20"
            v-model="checkboxGroup"
            type="is-info"
            :native-value="name"
          >
            {{ name }} ({{ value }} unique)
          </b-checkbox>
        </div>
        <p class="is-size-5 mb-4">Options</p>
        <div
          class="field"
        >
          <b-checkbox
            v-model="showAsPercentages"
            type="is-info"
            :native-value="1"
          >
            Show as percentages
          </b-checkbox>
        </div>
      </div>
      <div class="column is-four-fifths">
        <div class="table-container" v-if="showTable">
          <table class="table is-fullwidth">
            <thead>
              <tr>
                <th>{{ yTitle }}</th>
                <th v-for="label in yLabels" v-bind:key="label.id">
                  {{ label }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th>{{ xTitle }}</th>
                <td v-for="label in yLabels" v-bind:key="label.id">

                </td>
              </tr>
              <tr v-for="(values, index) in values" v-bind:key="values.id">
                <th>{{ index }}</th>
                <td v-for="metric in values" v-bind:key="metric.id">
                  {{ metric }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import authService from "../../services/authService";
import dataService from "../../services/dataService";

export default {
  name: "pivot",
  data() {
    return {
      filename: sessionStorage["sessionId"],
      timestamp: Date.now(),
      uri: authService.getEnvironmentURI(),
      checkboxGroup: [],
      showAsPercentages: [],
      showTable: false,
      yTitle: "",
      yLabels: [],
      xTitle: "",
      values: null
    };
  },
  computed: {
    nunique() {
      if (Object.keys(this.$store.state.metadata).length > 0) {
        return JSON.parse(this.$store.state.metadata.nunique);
      }
    }
  },
  methods: {
    async updateCrosstabData(x, y) {
      let showPercentages = (this.showAsPercentages.length === 0) ? 0 : 1;
      let data = await dataService.getCrosstab(x, y, showPercentages);
      this.yLabels = Object.keys(JSON.parse(data.crosstab));
      this.values = JSON.parse(data.transposed);
      this.showTable = true;
    }
  },
  watch: {
    checkboxGroup(arr) {
      if (arr.length === 2) {
        this.xTitle = this.checkboxGroup[0];
        this.yTitle = this.checkboxGroup[1];
        this.updateCrosstabData(this.xTitle, this.yTitle);
      } else {
        this.x = null;
        this.y = null;
        this.showTable = false;
      }
    },
    showAsPercentages(arr) {
      if (this.checkboxGroup.length === 2) {
        this.xTitle = this.checkboxGroup[0];
        this.yTitle = this.checkboxGroup[1];
        this.updateCrosstabData(this.xTitle, this.yTitle);
      }
    }
  }
};
</script>
