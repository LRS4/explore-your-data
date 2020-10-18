<template>
  <b-table :selected.sync="selected" :data="data" v-if="data && data.length > 0" hoverable>
    <b-table-column
      field="when"
      label="When..."
      width="33%"
      centred
      v-slot="props"
    >
      {{ props.row.when }}
    </b-table-column>

    <b-table-column
      field="when"
      :label="'... ' + target_column + ' had an average of...'"
      width="33%"
      centred
      v-slot="props"
    >
      {{ props.row.value }}
    </b-table-column>

    <b-table-column
      field="value"
      label="...which differs from the baseline average by..."
      width="33%"
      centred
      v-slot="props"
    >
      <b-progress
        type="is-info"
        :value="props.row.diff_from_baseline_avg"
        show-value
        :max="max_difference"
        size="is-medium"
      >
      </b-progress>
    </b-table-column>
  </b-table>
</template>

<script>
export default {
  name: "regression-table",
  props: {
    target_column: String,
    target_value: String,
    data: Array,
  },
  data() {
    return {
      selected: null,
    };
  },
  computed: {
    percentage_label() {
      return "... % with '".concat(
        String(this.target_column),
        "' value of ",
        String(this.target_value),
        " ..."
      );
    },
    max_difference() {
      return Math.max.apply(
        Math,
        this.data.map((a) => a.diff_from_baseline_avg)
      );
    },
  },
  watch: {
    selected() {
      this.$emit("selectedRow", this.selected);
    },
  },
};
</script>

<style>
.is-selected { 
  background-color: #005EA5 !important; 
  color: white !important;
}

.progress {
  background-color: blue !important;
}
</style>
