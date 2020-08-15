<template>
  <b-table :data="data" :columns="columns"></b-table>
</template>

<script>
export default {
  name: "table",
  props: {
    data: Array,
    columns: Array
  }
};
</script>
