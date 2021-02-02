<template>
  <b-table :data="data" :columns="columns" :sticky-header="true" height="700px"></b-table>
</template>

<script>
export default {
  name: "buefytable",
  props: {
    data: Array,
    columns: Array
  }
};
</script>
