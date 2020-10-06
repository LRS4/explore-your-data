<template>
  <section>
    <div class="columns" v-for="column in chunkedData" v-bind:key="column.id">
      <div class="column is-one-quarter" v-for="variable in column" v-bind:key="variable.id">
        <div class="card" :id="variable.name">
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img v-if="variable.type == 'Numeric'"
                  src="https://res.cloudinary.com/dayqxxsip/image/upload/v1601923068/Shared/1200px-Greek_uc_sigma.svg_hsngam.png" 
                  alt="Sigma symbol for numeric variable" />
                  <img v-else 
                  src="https://res.cloudinary.com/dayqxxsip/image/upload/v1601923065/Shared/category-icon-png-2_jhizjk.png"
                  alt="Boxes for categorical variable" />
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-4">{{ variable.name }}</p>
                <p class="subtitle is-6">{{ variable.type }}</p>
              </div>
            </div>

            <div class="content">
              <div class="columns">
                <div class="column">
                  <div class="mb-2" v-for="(data, name) in variable.data" v-bind:key="name.id">
                    <span class="has-text-weight-semibold">{{ name }} </span>
                    <span class="is-pulled-right">{{ data | toFixed }}</span>
                  </div>
                </div>
              </div>
            </div>
              <b-button tag="a" 
                :href="uri + 'api/plots/distribution/' + timestamp + '/' + filename + '/' + variable.name" 
                target="_blank" 
                class="button-secondary"
                v-if="lowUniqueValueCount(variable.name)">
                View distribution 
                <b-icon class="icon" icon="open-in-new" size="is-small"></b-icon>
              </b-button>
              <b-tooltip label="Too many unique values to plot" type="is-light" v-else>
                <b-button 
                  class="button-secondary"
                  disabled>
                  View distribution
                  <b-icon class="icon" icon="open-in-new" size="is-small"></b-icon>
                </b-button>
              </b-tooltip>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script> 
import authService from "../../services/authService";
var chunk = require("chunk");

export default {
  name: "univariate",
  data() {
    return {
      modalOpen: false,
      selectedImageUrl: null,
      filename: sessionStorage["sessionId"],
      timestamp: Date.now(),
      summary: [],
      chunkedData: null,
      uri: authService.getEnvironmentURI(),
      skipRenderingButton: false
    };
  },
  methods: {
    pushDataToSummaryArray(data, type) {
      for (let column in data) {
        this.summary.push({
          'type': type,
          'name': column,
          'data': data[column]
        });
      }
    },
    lowUniqueValueCount(variable) {
      let isCountLow = true;
      for (let i = 0; i < this.summary.length; i++) {
        let name = this.summary[i].name;
        let data = this.summary[i].data;
        if (data.unique > 15 && name === variable) {
          isCountLow = false;
        }
      }
      return isCountLow;
    }
  },
  created() {
    let numericSummary = JSON.parse(this.$store.state.dataset[0].dataset.num_describe);
    let categoricalSummary = JSON.parse(this.$store.state.dataset[0].dataset.cat_describe);
    this.pushDataToSummaryArray(numericSummary, 'Numeric');
    this.pushDataToSummaryArray(categoricalSummary, 'Categorical');
  },
  watch: {
    summary() {
      this.chunkedData = chunk(this.summary, 4);
    }
  },
  filters: {
    toFixed(value) {
      if (typeof (value) === 'number') {
        return value.toFixed(2);
      } else {
        return value;
      }
    }
  }
};
</script>

<style scoped>
img:hover {
  cursor: pointer;
}

.column, .card, .is-one-quarter {
  min-height: 300px !important;
}

.icon {
  margin-left: 1px !important;
}
</style>
