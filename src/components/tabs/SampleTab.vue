<template>
  <section>
    <span class="tag is-info mr-2">{{ shape.rows }} observations</span>
    <span class="tag is-info">{{ shape.columns }} variables</span>
    <Table :data="headRows" :columns="headColumns" />
  </section>
</template>

<script>
import Table from "@/components/Table.vue";
import { mapGetters } from "vuex";
import router from "../../router";
import dataService from "../../services/dataService";

export default {
  name: "analysis",
  components: {
    Table
  },
  data() {
    return {
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
    ...mapGetters(["headColumns", "headRows"]),
  },
};
</script>
