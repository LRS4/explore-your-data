<template>
  <section>
    <b-tabs v-model="activeTab" :animated="false" position="is-left">
      <b-tab-item class="tab" label="Data Preview">
        <span class="tag is-info mr-2">{{ shape.rows }} rows total</span>
        <span class="tag is-info">{{ shape.columns }} columns</span>
        <Table :data="rows" :columns="columns" />
      </b-tab-item>

      <b-tab-item label="Summary">
        <UnivariateTab />
      </b-tab-item>

      <b-tab-item label="Missing values">
        <MissingDataTab />
      </b-tab-item>
      
      <b-tab-item label="Bivariate">
        <BivariateTab />
      </b-tab-item>

      <b-tab-item label="Correlation"> 
        Coming soon. 
      </b-tab-item>

      <b-tab-item :visible="featureSwitch" label="Predictors">
        Coming soon.
      </b-tab-item>

      <b-tab-item :visible="featureSwitch" label="Next steps">
        Coming soon.
      </b-tab-item>
    </b-tabs>
  </section>
</template>

<script>
import Table from "@/components/Table.vue";
import UnivariateTab from "@/components/tabs/UnivariateTab.vue";
import BivariateTab from "@/components/tabs/BivariateTab.vue";
import MissingDataTab from '@/components/tabs/MissingDataTab.vue';
import { mapGetters } from "vuex";
import router from "../router";
import dataService from '../services/dataService';

export default {
  name: "analysis",
  components: {
    Table,
    UnivariateTab,
    BivariateTab,
    MissingDataTab
  },
  data() {
    return {
      activeTab: 0,
      featureSwitch: true,
      shape: {}
    };
  },
  created() {
    if (
      this.$store.state.dataset.length <= 0 ||
      this.$store.state.dataset === undefined
    ) {
      router.push({ path: "upload" });
    }
    this.getDataShape();
  },
  methods: {
    async getDataShape() {
      let shape = await dataService.getDataShape();
      this.shape = {
        'columns': shape.columns,
        'rows': shape.rows
      }
    }
  },
  computed: {
    dataset() {
      return this.$store.state.dataset[0].dataset;
    },
    ...mapGetters(["columns", "rows"]),
  },
};
</script>

<style lang="scss">
.tabs a {
  font-weight: 700 !important;
}

.tabs {
  background-color: #f8f8f8;
}
</style>
