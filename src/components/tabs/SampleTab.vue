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

export default {
  name: "analysis",
  components: {
    Table
  },
  computed: {
    ...mapGetters(["headColumns", "headRows"]),
    shape() {
      if (Object.keys(this.$store.state.metadata).length > 0) {
        return JSON.parse(this.$store.state.metadata.shape);
      }
    }
  },
};
</script>
