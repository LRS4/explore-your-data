<template>
  <section>
    <div class="columns" v-for="column in chunkedData" v-bind:key="column.id">
      <div class="column is-one-third" v-for="variable in column" v-bind:key="variable.id">
        <div class="card">
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img v-if="variable.type == 'Numeric'"
                  src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Greek_uc_sigma.svg/1200px-Greek_uc_sigma.svg.png" 
                  alt="Sigma symbol for numeric variable" />
                  <img v-else 
                  src="https://icon-library.com/images/category-icon-png/category-icon-png-2.jpg"
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
                  <p class="has-text-weight-semibold" v-for="(data, name) in variable.data" v-bind:key="name.id">
                    {{ name }}
                  </p>
                </div>
                <div class="column">
                  <p v-for="(data, name) in variable.data" v-bind:key="name.id">
                    {{ data }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import dataService from "../../services/dataService";
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
      chunkedData: null
    };
  },
  created() {
    this.returnDataSummary();
  },
  components: {},
  methods: {
    async returnDataSummary() {
      await this.returnNumericSummary();
      await this.returnCategoricalSummary();
      this.chunkDataSummary();
    },
    chunkDataSummary() {
      this.chunkedData = chunk(this.summary, 3);
    },
    async returnNumericSummary() {
      let data = await dataService.getNumericVariablesSummary();
      this.pushDataToSummary(data, 'Numeric');
    },
    async returnCategoricalSummary() {
      let data = await dataService.getCategoricalVariablesSummary();
      this.pushDataToSummary(data, 'Categorical');
    },
    pushDataToSummary(data, type) {
      for (let column in data) {
        this.summary.push({
          'type': type,
          'name': column,
          'data': data[column]
        });
      }
    }
  }
};
</script>

<style scoped>
img:hover {
  cursor: pointer;
}

.column, .is-one-third {
  min-height: 350px;
}
</style>
