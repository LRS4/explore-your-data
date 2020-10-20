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
      field="percentage"
      :label="percentage_label"
      width="33%"
      centred
      v-slot="props"
    >
      <b-progress
        type="is-info"
        :value="props.row.percentage"
        show-value
        size="is-medium"
        format="percent"
      >
      </b-progress>
    </b-table-column>
  </b-table>
</template>

<script>
export default {
  name: "classification-table",
  props: {
    target_column: String,
    target_value: String,
    data: Array
  },
  data() {
    return {
      selected: null
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
    }
  },
  watch: {
    selected() {
      this.$emit('selectedRow', this.selected);
    }
  }
};
</script>

<style>
.is-selected { 
    background-color: #005EA5 !important; 
    color: white !important;
}
</style>
