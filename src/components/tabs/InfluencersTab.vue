<template>
  <section>
    <div class="select-analysis-type" v-show="analysisType == null">
      <h3 class="is-size-5 mb-4">
        What type of analysis do you want to carry out?
      </h3>

      <div class="columns">
        <div class="column">
          <div class="card-button app-promo--grey">
            <a
              class="card-button__link-wrapper"
              href="#/analysis"
              @click="setAnalysisType('categorical')"
            >
              {{ analysisType }}
              <img
                class="card-button__img"
                src="https://s16353.pcdn.co/wp-content/uploads/2019/05/tree-feature.jpg"
                alt=""
                style="height: 300px"
              />
              <div class="card-button__content">
                <h3 class="card-button__heading">Categorical</h3>
                <p class="card-button__description">
                  What influences this to be A or B? Segments the data to
                  uncover influencers on the target variable and target value
                  for classification models.
                </p>
              </div>
            </a>
          </div>
        </div>
        <div class="column">
          <div class="card-button app-promo--grey">
            <a
              class="card-button__link-wrapper"
              href="#/analysis"
              @click="setAnalysisType('continuous')"
            >
              <img
                class="card-button__img"
                src="https://cutewallpaper.org/21/wallpaper-graph/Abstract-Financial-Chart-With-Uptrend-Line-Graph-On-Blue-.jpg"
                alt=""
                style="height: 300px"
              />
              <div class="card-button__content">
                <h3 class="card-button__heading">Continuous</h3>
                <p class="card-button__description">
                  What influences this to increase or decrease? Segments the
                  data to uncover influencers on the target variable for
                  regression models.
                </p>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>

    <div class="main-section" v-show="analysisType != null">
      <a href="#/analysis" @click="goBack" class="link back-link">
        <b-icon icon="chevron-left" size="is-small"></b-icon>Back
      </a>
      <div class="columns is-vcentred">
        <div class="column pt-0 mt-4">
          <p class="is-size-5 mb-2 mt-2"></p>
          <b-message type="is-info">
            Select a variable and target value below
          </b-message>
          <span class="text-bottom">What influences... </span>

          <b-dropdown v-model="currentVariable" aria-role="list">
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
              v-for="(value, name) in nunique"
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
          />
        </div>
        <div class="column is-one-half pt-0 mt-4">
          <b-message class="mt-2" type="is-info" v-if="influencers != null">
            Select a row in the table for more information.
          </b-message>

          <div class="field" v-if="selectedRow != null">
              <b-checkbox
                v-model="showActuals"
                type="is-info"
                :native-value="1"
              >
                Show actuals (default is percentages)
              </b-checkbox>
          </div>

          <b-image
            class="mt-6"
            v-bind:src="uri + 'api/plots/influencer-plot/' + timestamp + '/' + filename + '/' + selectedRow.column + '/' + currentVariable + '/' + currentTargetValue + '/' + actuals"
            placeholder="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png"
            webp-fallback=".jpg"
            ratio="15by11"
            v-if="selectedRow != null && currentTargetValue != 'Select value'"
          >
          </b-image>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import authService from "../../services/authService";
import dataService from "../../services/dataService";
import influencerService from "../../services/influencerService";
import ClassificationTable from "@/components/ClassificationTable.vue";

export default {
  name: "influencers",
  components: {
    ClassificationTable,
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
      actuals: 0
    };
  },
  methods: {
    setAnalysisType(type) {
      if (type === "continuous") {
        this.uniqueValues = ["Increase", "Decrease"];
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
      return data.map((obj) => {
        return {
          when: `${obj.parent_column_name} is ${obj.index}`,
          percentage: obj.value,
          column: obj.parent_column_name,
        };
      });
    },
    prepareContinuousInfluencers(data) {
      return data;
    },
  },
  computed: {
    firstColumn() {
      return this.menus[0];
    },
    nunique() {
      let newObject = {};
      let nunique = JSON.parse(this.$store.state.dataset[0].dataset.nunique);
      for (let key in nunique) {
        if (nunique[key] < 20) {
          newObject[key] = nunique[key];
        }
      }
      return newObject;
    },
    currentTargetValueType() {
      return typeof this.currentTargetValue;
    },
  },
  watch: {
    async currentVariable(value) {
      if (this.analysisType === "categorical" && value !== "Select variable") {
        let uniqueValues = await dataService.getUniqueValues(value);
        this.uniqueValues = uniqueValues["uniques"];
      }
    },
    uniqueValues() {
      if (this.uniqueValues.length > 0) {
        this.currentTargetValue = "Select value";
      }
    },
    async currentTargetValue(value) {
      if (value !== "Select value") {
        console.log("Getting key influencers...");
        let res = await influencerService.getKeyInfluencers(
          this.analysisType,
          this.currentVariable,
          this.currentTargetValue
        );

        if (this.analysisType === "continuous") {
          this.influencers = this.prepareContinuousInfluencers(res.influencers);
        } else {
          this.influencers = this.prepareCategoricalInfluencers(
            res.influencers
          );
          console.log(this.influencers);
        }
      }
    },
    showActuals(arr) {
      if (arr.length > 0) {
        this.actuals = 1;
      } else {
        this.actuals = 0;
      }
    }
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

.card-button {
  margin-bottom: 36px;
  width: 100%;
}

.card-button__link-wrapper {
  background-color: #fff;
  border: 1px solid transparent;
  box-shadow: 0 4px 0 0 #d8dde0;
  display: block;
  height: 100%;
  position: relative;
  text-decoration: none;
  color: #005ea5;
}

.card-button__link-wrapper:hover {
  background-color: #fff;
  color: #005eb8;
}

.card-button__link-wrapper:hover .card-button__heading {
  color: #7c2855;
}

.card-button__link-wrapper:focus {
  background-color: #fff;
  box-shadow: 0 4px 0 0 #d8dde0;
}

.card-button__link-wrapper:focus .card-button__heading {
  background-color: #ffeb3b;
  box-shadow: 0 -2px #ffeb3b, 0 4px #212b32;
  color: #212b32;
  outline: 4px solid transparent;
  text-decoration: none;
}

.card-button__link-wrapper:active {
  background-color: #fff;
  box-shadow: none;
  top: 4px;
}

.card-button__link-wrapper:active .card-button__heading {
  background: 0 0;
  box-shadow: none;
}

.card-button__link-wrapper:active .card-button__heading,
.card-button__link-wrapper:hover .card-button__heading {
  text-decoration: none;
}

.card-button__img {
  border-bottom: 1px solid #f0f4f5;
  display: block;
  width: 100%;
}

@media print {
  .card-button__img {
    display: none;
  }
}

.card-button__heading {
  font-weight: 600;
  font-size: 20px;
  font-size: 1.25rem;
  line-height: 1.4;
  display: inline-block;
  margin-bottom: 16px;
  text-decoration: underline;
}

@media (min-width: 40.0625em) {
  .card-button__heading {
    font-size: 24px;
    font-size: 1.5rem;
    line-height: 1.33333;
  }
}

@media print {
  .card-button__heading {
    font-size: 18pt;
    line-height: 1.15;
  }
}

.card-button__content {
  padding: 24px;
}

.card-button__content > :first-child {
  margin-top: 0;
}

.card-button__content > :last-child {
  margin-bottom: 0;
}

@media (min-width: 40.0625em) {
  .card-button__content {
    padding: 32px;
  }
}

.card-button__description {
  color: #4c6272;
}

.card-button--small .card-button__heading {
  font-size: 16px;
  font-size: 1rem;
  line-height: 1.5;
}

@media (min-width: 40.0625em) {
  .card-button--small .card-button__heading {
    font-size: 19px;
    font-size: 1.1875rem;
    line-height: 1.47368;
  }
}

@media print {
  .card-button--small .card-button__heading {
    font-size: 14pt;
    line-height: 1.15;
  }
}

.card-button--small .card-button__description {
  font-size: 14px;
  font-size: 0.875rem;
  line-height: 1.71429;
}

@media (min-width: 40.0625em) {
  .card-button--small .card-button__description {
    font-size: 16px;
    font-size: 1rem;
    line-height: 1.5;
  }
}

@media print {
  .card-button--small .card-button__description {
    font-size: 14pt;
    line-height: 1.2;
  }
}

.card-button-group {
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 36px;
}

@media (max-width: 48.0525em) {
  .card-button-group {
    margin-bottom: 28px;
  }
}

.card-button-group__item {
  display: flex;
}

@media (max-width: 48.0525em) {
  .card-button-group__item {
    flex: 0 0 100%;
  }
}

@media (max-width: 48.0525em) {
  .card-button-group__item {
    margin-bottom: 28px;
  }

  .card-button-group__item:last-child {
    margin-bottom: 0;
  }
}

.card-button-group__item .card-button {
  margin-bottom: 0;
}
</style>
