<template>
  <section>
    <b-tabs v-model="activeTab" :animated="false" position="is-left">
      <b-tab-item class="tab" label="Overview">
        <OverviewTab />
      </b-tab-item>
      
      <b-tab-item class="tab" label="Data Sample">
        <SampleTab />
      </b-tab-item>

      <b-tab-item label="Variables">
        <UnivariateTab />
      </b-tab-item>

      <b-tab-item label="Interactions">
        <BivariateTab />
      </b-tab-item>

      <b-tab-item label="Correlation"> 
        <CorrelationTab />
      </b-tab-item>

      <b-tab-item label="Crosstab"> 
        <PivotTab />
      </b-tab-item>

      <b-tab-item label="Missing values">
        <MissingDataTab />
      </b-tab-item>

      <b-tab-item label="Influencers">
        <InfluencersTab />
      </b-tab-item>

      <b-tab-item :visible="featureSwitch" label="Next steps">
        <NextStepsTab />
      </b-tab-item>
    </b-tabs>
  </section>
</template>

<script>
import Table from "@/components/Table.vue";
import OverviewTab from "@/components/tabs/OverviewTab.vue";
import SampleTab from "@/components/tabs/SampleTab.vue";
import UnivariateTab from "@/components/tabs/UnivariateTab.vue";
import BivariateTab from "@/components/tabs/BivariateTab.vue";
import MissingDataTab from '@/components/tabs/MissingDataTab.vue';
import CorrelationTab from '@/components/tabs/CorrelationTab.vue';
import PivotTab from '@/components/tabs/PivotTab.vue';
import InfluencersTab from '@/components/tabs/InfluencersTab.vue';
import NextStepsTab from '@/components/tabs/NextStepsTab.vue';

export default {
  name: "analysis",
  components: {
    Table,
    OverviewTab,
    SampleTab,
    UnivariateTab,
    BivariateTab,
    MissingDataTab,
    CorrelationTab,
    PivotTab,
    InfluencersTab,
    NextStepsTab
  },
  data() {
    return {
      activeTab: 0,
      featureSwitch: true
    };
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
