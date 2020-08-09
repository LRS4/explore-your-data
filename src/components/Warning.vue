/* eslint-disable semi */
<template>
  <section>
    <div class="warning">
        <div class="content">
            <p><b-icon class="alert-circle" icon="alert-circle" size="is-medium"></b-icon> {{ message }}</p>
        </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'warning',
  props: {
    message: String
  }
};
</script>

<style scoped lang="scss">
.warning {
    margin-bottom: 30px;
}

.content {
    margin: 10px;
    color: black;
    font-weight: bold;
}

.alert-circle {
    vertical-align: bottom !important;
}
</style>
