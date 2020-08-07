<template>
  <div>
    <div class="thin-blue-strip" />
    <div class="has-text-left help-section">
      <h1 class="is-size-4 has-text-weight-bold content">Useful resources</h1>
      <ul>
        <li>
          <a class="link"
            href="https://analystsuncertaintytoolkit.github.io/UncertaintyWeb/introduction.html"
            target="_blank">
            Uncertainty toolkit
          </a>
        </li>
        <li>
          <a class="link"
            href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/416478/aqua_book_final_web.pdf"
            target="_blank">
            Aqua Book
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Help",
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}

p,
ul {
  font-size: 19px;
}

.thin-blue-strip {
  height: 10px;
  background-color: #005ea5;
  margin-top: -1px;
  position: relative;
  z-index: -1;
}
</style>
