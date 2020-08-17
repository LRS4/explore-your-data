<template>
  <section>
    <b-tabs v-model="activeTab" :animated="false">
      <b-tab-item class="tab" label="Data">
        <Table :data="rows" :columns="columns" />
      </b-tab-item>

      <b-tab-item class="tab" label="Summary">
        {{ summary }}
      </b-tab-item>

      <b-tab-item label="Univariate">
        What light is light, if Silvia be not seen?
        <br />What joy is joy, if Silvia be not by—
        <br />Unless it be to think that she is by
        <br />And feed upon the shadow of perfection?
        <br />Except I be by Silvia in the night,
        <br />There is no music in the nightingale.
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
import { mapGetters } from 'vuex';
import router from '../router';
import $backend from '../backend';

export default {
  name: "analysis",
  components: {
    Table
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
      console.log("done");
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
