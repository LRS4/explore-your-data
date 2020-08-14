<template>
  <div class="home">
    <BackLink />
    <div class="columns">
      <div class="column is-two-thirds">
        <h1 class="is-size-1 has-text-weight-bold content">Upload data</h1>
        <Notification
          v-if="showError"
          type="error"
          title="There is a problem"
          :message="errorMessage"
        />
        <Warning message="Only upload data which is not sensitive, or has been anonymised." />
        <FileUploader
          @showError="showError = $event"
          @errorMessage="errorMessage = $event"
          @dataValid="isButtonDisabled = $event"
          @data="data = $event"
        />
        <b-button
          class="is-success button has-text-weight-bold"
          size="is-medium"
          data-prevent-double-click
          :rounded="false"
          :disabled="isButtonDisabled"
          @click="submitData"
        >Continue</b-button>
      </div>
    </div>
    <Spinner :isLoading="isLoading" />
  </div>
</template>

<script>
// @ is an alias to /src
import FileUploader from "@/components/FileUploader.vue";
import Warning from "@/components/Warning.vue";
import Notification from "@/components/Notification.vue";
import Spinner from "@/components/Spinner.vue";
import BackLink from "@/components/BackLink.vue";
import $backend from '../backend'
import router from '../router'

export default {
  name: "upload",
  components: {
    FileUploader,
    Warning,
    Notification,
    Spinner,
    BackLink
  },
  data() {
    return {
      showError: false,
      errorMessage: "The file must be in CSV (comma-separated values) format.",
      isButtonDisabled: true,
      isLoading: false,
      data: null,
    };
  },
  methods: {
    submitData() {
      console.log("Submitting data...");
      this.isLoading = true;
      $backend.uploadFile(this.data)
        .then(res => {
          if (res === "Invalid data") {
            this.showError = true;
            this.isLoading = false;
            this.errorMessage = "The uploaded data was invalid.";
          } else {
            this.$store.dispatch('setDataset', {
              dataset: res
            });
            router.push('analysis');
          }
        });
    }
  },
};
</script>

<style scoped>
.columns {
  margin-top: 5px;
}
</style>
