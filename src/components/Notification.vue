/* eslint-disable semi */
<template>
  <section>
    <div class="error-box">
        <div class="content">
            <h3>{{ title }}</h3>
            <p>{{ message }}</p>
        </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'notification',
  props: {
    type: String,
    title: String,
    message: String
  }
};
</script>

<style scoped lang="scss">
.error-box {
    border: 5px solid #D4351C;
    margin-bottom: 30px;
}

.content {
    margin: 10px;
    color: #D4351C;
    font-weight: bold;
}
</style>
