<template>
  <section>
    <SelectAnalysis
      v-show="analysisType == null"
      @analysisType="
        analysisType = $event;
        setAnalysisType($event);
      "
    />

    <div class="main-section" v-show="analysisType != null">
      <a href="#/analysis/influencers" @click="goBack" class="link back-link">
        <b-icon icon="chevron-left" size="is-small"></b-icon>Back
      </a>
      <div class="columns is-vcentred">
        <div class="column pt-0 mt-4">
          <p class="is-size-5 mb-2 mt-2"></p>
          <b-message type="is-info">
            Select a variable and target value below
          </b-message>
          <span class="text-bottom">What influences... </span>

          <b-dropdown v-model="currentVariable" aria-role="list" @change="showImage = false">
            <b-button
              class="button button-secondary"
              type="is-text is-small"
              slot="trigger"
            >
              <template>
                <span>{{ currentVariable }}</span>
              </template>
              <b-icon icon="menu-down"></b-icon>
            </b-button>

            <b-dropdown-item
              v-for="(value, name) in selectVariableList"
              v-bind:key="value.id"
              :value="name"
              aria-role="listitem"
              class="is-secondary"
            >
              <h3>{{ name }}</h3>
            </b-dropdown-item>
          </b-dropdown>

          <span class="text-bottom" v-if="analysisType == 'continuous'">
            ...to...
          </span>
          <span class="text-bottom" v-else> ...to be... </span>

          <b-dropdown v-model="currentTargetValue" aria-role="list">
            <b-button
              class="button button-secondary"
              type="is-text is-small"
              slot="trigger"
            >
              <template>
                <span>{{ currentTargetValue }}</span>
              </template>
              <b-icon icon="menu-down"></b-icon>
            </b-button>

            <b-dropdown-item
              v-for="(value, index) in uniqueValues"
              :key="index"
              :value="value"
              aria-role="listitem"
              class="is-secondary"
            >
              <h3>{{ value }}</h3>
            </b-dropdown-item>
          </b-dropdown>

          <hr />

          <ClassificationTable
            :target_column="currentVariable"
            :target_value="String(currentTargetValue)"
            :data="influencers"
            @selectedRow="selectedRow = $event"
            v-if="
              analysisType == 'categorical' &&
              currentTargetValue != 'Select value'
            "
          />

          <RegressionTable
            class="mt-4"
            :target_column="currentVariable"
            :target_value="String(currentTargetValue)"
            :data="influencers"
            @selectedRow="selectedRow = $event"
            v-if="
              analysisType == 'continuous' &&
              currentTargetValue != 'Select value'
            "
          />
        </div>
        <div class="column is-one-half pt-0 mt-4">
          <b-message
            class="mt-2"
            type="is-info"
            v-if="influencers != null && currentTargetValue != 'Select value'"
          >
            Select a row in the table for more information.
          </b-message>

          <div class="field" v-if="selectedRow != null">
            <b-checkbox
              v-model="showActuals"
              type="is-info"
              :native-value="1"
              v-if="
                selectedRow != null &&
                currentTargetValue != 'Select value' &&
                analysisType === 'categorical'
              "
            >
              Show target counts
              <b-tooltip 
                label="
                  Default is percentages for categorical target values
                  and averages for numeric target values.
                "
                position="is-bottom"
                type="is-info">
                <b-icon
                  icon="help-circle"
                  size="is-small"
                  type="is-info">
                </b-icon>
              </b-tooltip>
            </b-checkbox>
          </div>

          <b-image
            class="mt-6"
            v-bind:src="
              uri +
              'api/plots/influencer-plot/' +
              timestamp +
              '/' +
              filename +
              '/' +
              selectedRow.column +
              '/' +
              currentVariable +
              '/' +
              currentTargetValue +
              '/' +
              analysisType +
              '/' +
              actuals
            "
            placeholder="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png"
            webp-fallback=".jpg"
            ratio="15by11"
            v-if="
              selectedRow != null &&
              currentTargetValue != 'Select value' &&
              analysisType != null &&
              showImage == true
            "
          >
          </b-image>

          <b-message
            class="mt-6 warning-message"
            type="is-warning"
            has-icon
            v-model="showWarning"
            v-if="
              selectedRow != null &&
              currentTargetValue != 'Select value' &&
              analysisType != null
            "
          >
            {{ warningMsg }} Select another row in the table to
            refresh the plot.
          </b-message>
        </div>
      </div>
    </div>

    <Spinner :isLoading="isLoading" />
  </section>
</template>

<script>
import authService from "@/services/authService";
import dataService from "@/services/dataService";
import influencerService from "@/services/influencerService";
import ClassificationTable from "@/components/tabs/InfluencersTab/ClassificationTable.vue";
import RegressionTable from "@/components/tabs/InfluencersTab/RegressionTable.vue";
import SelectAnalysis from "@/components/tabs/InfluencersTab/SelectAnalysis.vue";
import Spinner from "@/components/Spinner.vue";

export default {
  name: "influencers",
  components: {
    ClassificationTable,
    RegressionTable,
    SelectAnalysis,
    Spinner,
  },
  data() {
    return {
      filename: sessionStorage["sessionId"],
      timestamp: Date.now(),
      uri: authService.getEnvironmentURI(),
      analysisType: null,
      currentVariable: "Select variable",
      currentTargetValue: "",
      uniqueValues: [],
      influencers: null,
      selectedRow: null,
      showActuals: [],
      actuals: 0,
      isLoading: false,
      showImage: false,
      showWarning: false,
      warningMsg: ""
    };
  },
  methods: {
    setAnalysisType(type) {
      if (type === "continuous") {
        this.currentVariable = "Select variable";
        this.currentTargetValue = "Select value";
        this.uniqueValues = [];
      } else {
        this.currentVariable = "Select variable";
        this.currentTargetValue = "Select value";
        this.uniqueValues = [];
      }
      this.analysisType = type;
    },
    goBack() {
      this.analysisType = null;
    },
    prepareCategoricalInfluencers(data) {
      // Format: { 'when': 'Sex is female...', 'percentage': 74, 'column': 'Sex' }
      return data.map((obj) => {
        let index = (obj.index)
          .replace('(', '')
          .replace(']', '')
          .replace(',', ' -');
        return {
          when: `${obj.parent_column_name} is ${index}`,
          percentage: obj.value,
          column: obj.parent_column_name,
        };
      });
    },
    prepareContinuousInfluencers(data) {
      // Format: { 'when': 'ptratio is between 239 - 292', 'value': 50, 'diff_from_baseline_avg': 27.47, 'column': 'Ptratio' }
      return data.map((obj) => {
        let index = (obj.index)
          .replace('(', '')
          .replace(']', '')
          .replace(',', ' -');
        return {
          when: `${obj.parent_column_name} is ${index}`,
          value: obj.value,
          diff_from_baseline_avg: obj.difference_from_baseline_avg,
          column: obj.parent_column_name,
        };
      });
    },
    checkForHighNunique(value) {
      let column = value.column;
      let valueIsCategorical = Object.keys(this.catDescribe).includes(
        String(column)
      );
      if (valueIsCategorical) {
        let nunique = this.catDescribe[column]["unique"]
        let categoryHasHighNunique = nunique > 15;
        if (categoryHasHighNunique) {
          this.showImage = false;
          this.warningMsg = `
            ${column} has too many unique 
            values (${nunique}) to plot. 
          `;
          this.showWarning = true;
        } else {
          this.showWarning = false;
          setTimeout(() => {
            this.showImage = true;
          }, 500);
        }
      } else {
        this.showWarning = false;
        setTimeout(() => {
          this.showImage = true;
        }, 500);
      }
    },
  },
  computed: {
    getCategoricalDropdownItems() {
      if (Object.keys(this.$store.state.metadata).length > 0) {
        let newObject = {};
        let nunique = JSON.parse(this.$store.state.metadata.nunique);
        for (let key in nunique) {
          if (nunique[key] < 20) {
            newObject[key] = nunique[key];
          }
        }
        return newObject;
      }
    },
    getContinuousDropdownItems() {
      if (Object.keys(this.$store.state.metadata).length > 0) {
        return JSON.parse(this.$store.state.metadata.num_describe);
      }
    },
    catDescribe() {
      if (Object.keys(this.$store.state.metadata).length > 0) {
        return JSON.parse(this.$store.state.metadata.cat_describe);
      }
    },
    selectVariableList() {
      if (this.analysisType === "categorical") {
        return this.getCategoricalDropdownItems;
      } else {
        return this.getContinuousDropdownItems;
      }
    },
    currentTargetValueType() {
      return typeof this.currentTargetValue;
    },
  },
  watch: {
    async currentVariable(value) {
      if (this.analysisType === "categorical" && value !== "Select variable") {
        this.isLoading = true;
        let uniqueValues = await dataService.getUniqueValues(value);
        this.uniqueValues = uniqueValues["uniques"].filter(value => value !== 'Missing');
        this.isLoading = false;
      }

      if (this.analysisType === "continuous" && value !== "Select variable") {
        this.currentTargetValue = "Select value";
        this.uniqueValues = ["Increase", "Decrease"];
      }
    },
    uniqueValues() {
      if (this.uniqueValues.length > 0) {
        this.currentTargetValue = "Select value";
      }
    },
    async currentTargetValue(value) {
      if (value !== "Select value" && value !== null) {
        console.log("Getting key influencers...");
        this.isLoading = true;
        this.selectedRow = null;

        let res = await influencerService.getKeyInfluencers(
          this.analysisType,
          this.currentVariable,
          this.analysisType === "categorical"
            ? this.currentTargetValue
            : this.currentTargetValue.toLowerCase()
        );

        if (this.analysisType === "continuous") {
          this.influencers = this.prepareContinuousInfluencers(res.influencers);
        } else {
          this.influencers = this.prepareCategoricalInfluencers(
            res.influencers
          );
        }
        this.isLoading = false;
      }
    },
    selectedRow(value) {
      if (value != null) {
        this.checkForHighNunique(value);
      }
    },
    showActuals(arr) {
      if (arr.length > 0) {
        this.actuals = 1;
      } else {
        this.actuals = 0;
      }
    },
  },
};
</script>

<style scoped>
.text-bottom {
  vertical-align: bottom;
}

.dropdown-item:focus {
  background-color: white;
}

.is-active {
  background-color: #1d70b8 !important;
}

.warning-message {
  margin-top: 75px !important;
}
</style>
