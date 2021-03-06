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
import authService from "../services/authService";
import uploadService from "../services/uploadService";
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
    async submitData() {
      console.log("Submitting data...");
      this.isLoading = true;
      if (!this.sessionIdHasBeenSet()) {
        await authService.getUniqueSessionId();
      }
      this.handleFileSubmit();
    },
    handleFileSubmit() {
      uploadService.uploadFile(this.data)
        .then(res => {
          if (res === "Invalid data") {
            this.showErrorMessage("The uploaded data was invalid.");
          } 

          if (res != null && res !== undefined) {
            this.sendMetadataToStore(res);
          } else {
            this.showErrorMessage("Upload failed. Please try uploading the CSV again.");
          }
        });
    },
    showErrorMessage(message) {
      this.showError = true;
      this.isLoading = false;
      this.errorMessage = message;
    },
    sendMetadataToStore(res) {
      this.$store.dispatch('setMetadata', {
        metadata: res
      });
      console.log('Metadata pushed to store:', res);
      this.goToAnalysisPage();
    },
    goToAnalysisPage() {
      router.push('analysis/overview');
    },
    sessionIdHasBeenSet() {
      return sessionStorage['sessionId'] !== undefined;
    }
  }
};
</script>

<style scoped>
.columns {
  margin-top: 5px;
}
</style>
