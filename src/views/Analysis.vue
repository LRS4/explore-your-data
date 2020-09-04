<template>
  <section>
    <b-tabs v-model="activeTab" :animated="false">
      <b-tab-item class="tab" label="Data">
        <Table :data="rows" :columns="columns" />
      </b-tab-item>

      <b-tab-item class="tab" label="Summary">
        <div v-for="(column, title) in summary" v-bind:key="column.id">
          <h1>{{ title }}</h1>
          <ul>
            <li v-for="(value, measure) in column" v-bind:key="value.id">
              {{ measure }} - {{ value }}
            </li>
          </ul>
        </div>
      </b-tab-item>

      <b-tab-item label="Univariate">
        <UnivariateTab />
      </b-tab-item>

      <b-tab-item label="Bivariate">
        Nunc nec velit nec libero vestibulum eleifend.
        Curabitur pulvinar congue luctus.
        Nullam hendrerit iaculis augue vitae ornare.
        Maecenas vehicula pulvinar tellus, id sodales felis lobortis eget.
      </b-tab-item>

      <b-tab-item label="Multivariate">
        Nunc nec velit nec libero vestibulum eleifend.
        Curabitur pulvinar congue luctus.
        Nullam hendrerit iaculis augue vitae ornare.
        Maecenas vehicula pulvinar tellus, id sodales felis lobortis eget.
      </b-tab-item>

      <b-tab-item label="Correlation">
        Nunc nec velit nec libero vestibulum eleifend.
        Curabitur pulvinar congue luctus.
        Nullam hendrerit iaculis augue vitae ornare.
        Maecenas vehicula pulvinar tellus, id sodales felis lobortis eget.
      </b-tab-item>

      <b-tab-item :visible="featureSwitch" label="Analysis">
        Nunc nec velit nec libero vestibulum eleifend.
        Curabitur pulvinar congue luctus.
        Nullam hendrerit iaculis augue vitae ornare.
        Maecenas vehicula pulvinar tellus, id sodales felis lobortis eget.
      </b-tab-item>

      <b-tab-item :visible="featureSwitch" label="Time Series">
        Nunc nec velit nec libero vestibulum eleifend.
        Curabitur pulvinar congue luctus.
        Nullam hendrerit iaculis augue vitae ornare.
        Maecenas vehicula pulvinar tellus, id sodales felis lobortis eget.
      </b-tab-item>

    </b-tabs>

  </section>
</template>

<script>
import Table from "@/components/Table.vue";
import UnivariateTab from "@/components/UnivariateTab.vue";
import { mapGetters } from 'vuex';
import router from '../router';
import $backend from '../backend';

export default {
  name: "analysis",
  components: {
    Table,
    UnivariateTab
  },
  data() {
    return {
      activeTab: 0,
      featureSwitch: true,
      summary: null
    };
  },
  created() {
    if (this.$store.state.dataset.length <= 0 || this.$store.state.dataset === undefined) {
      router.push({ path: 'upload' });
    }

    this.returnDataSummary();
  },
  methods: {
    async returnDataSummary() {
      this.summary = await $backend.getDataSummary();
      console.log(this.summary);
    }
  },
  computed: {
    dataset() {
      return this.$store.state.dataset[0].dataset;
    },
    ...mapGetters([
      'columns',
      'rows'
    ])
  }
};
</script>

<style lang="scss">
.tabs a {
  font-weight: 700 !important;
}

.tabs {
  background-color: #F8F8F8;
}
</style>
