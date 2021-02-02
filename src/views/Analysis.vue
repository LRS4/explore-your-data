<template>
  <section>
    <div class="tabs">
      <ul>
        <router-link active-class="is-active" tag="li" to="overview" exact>
          <a>Overview</a>
        </router-link>
        <router-link active-class="is-active" tag="li" to="sample" exact>
          <a>Data Sample</a>
        </router-link>
        <router-link active-class="is-active" tag="li" to="variables">
          <a>Variables</a>
        </router-link>
        <router-link active-class="is-active" tag="li" to="interactions">
          <a>Interactions</a>
        </router-link>
        <router-link active-class="is-active" tag="li" to="correlation">
          <a>Correlation</a>
        </router-link>
        <router-link active-class="is-active" tag="li" to="crosstab">
          <a>Crosstab</a>
        </router-link>
        <router-link active-class="is-active" tag="li" to="missing">
          <a>Missing values</a>
        </router-link>
        <router-link active-class="is-active" tag="li" to="influencers">
          <a>Influencers</a>
        </router-link>
        <router-link active-class="is-active" tag="li" to="next-steps">
          <a>Next steps</a>
        </router-link>
      </ul>
    </div>

    <keep-alive>
      <router-view></router-view>
    </keep-alive>
  </section>
</template>

<script>
import Table from "@/components/Table.vue";
import OverviewTab from "@/components/tabs/OverviewTab.vue";
import SampleTab from "@/components/tabs/SampleTab.vue";
import UnivariateTab from "@/components/tabs/UnivariateTab.vue";
import BivariateTab from "@/components/tabs/BivariateTab.vue";
import MissingDataTab from "@/components/tabs/MissingDataTab.vue";
import CorrelationTab from "@/components/tabs/CorrelationTab.vue";
import PivotTab from "@/components/tabs/PivotTab.vue";
import InfluencersTab from "@/components/tabs/InfluencersTab/InfluencersTab.vue";
import NextStepsTab from "@/components/tabs/NextStepsTab.vue";
import router from "../router";
import authService from '../services/authService';

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
      featureSwitch: true,
      filename: sessionStorage["sessionId"],
      timestamp: Date.now(),
      uri: authService.getEnvironmentURI()
    };
  },
  beforeCreate() {
    if (Object.keys(this.$store.state.metadata).length <= 0) {
      router.push({ name: "upload" });
    }
  },
  mounted() {
    this.preloadImage(this.uri + 'api/plots/missing-data-plot/' + this.timestamp + '/' + this.filename);
  },
  methods: {
    preloadImage(url) {
      var img = new Image();
      img.src = url;
      this.$store.dispatch('cacheImage', {
        name: 'missingDataImg',
        img: img 
      });
    }
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
