<template>
  <section>
    <div class="columns">
      <div class="column">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Dataset statistics</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>Number of variables</th>
              <td>{{ metadata.variables }}</td>
            </tr>
            <tr>
              <th>Number of observations</th>
              <td>{{ metadata.observations }}</td>
            </tr>
            <tr>
              <th>Missing cells</th>
              <td>{{ metadata.totalMissingValues }}</td>
            </tr>
            <tr>
              <th>Missing cells (%)</th>
              <td>{{ metadata.totalMissingPercent }} %</td>
            </tr>
            <tr>
              <th>Duplicate rows</th>
              <td>{{ metadata.totalDuplicatedRows }}</td>
            </tr>
            <tr>
              <th>Duplicate rows (%)</th>
              <td>{{ metadata.totalDuplicatedPercent }} %</td>
            </tr>
            <tr>
              <th>Total size in memory (Kb)</th>
              <td>{{ metadata.totalKbInMemory }} Kb</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="column">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Warnings</th>
              <th>Type</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="warning in metadata.warningMessages" v-bind:key="warning.id">
              <td>
                <b-tag type="is-warning">{{ warning.column }}</b-tag> {{ warning.message }}
              </td>
              <td>
                <b-tag type="is-light">{{ warning.type }}</b-tag>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "overview",
  data() {
    return {
      filename: sessionStorage["sessionId"],
      timestamp: Date.now()
    };
  },
  computed: {
    metadata() {
      return this.$store.state.metadata.metadata;
    }
  }
};
</script>

<style>

</style>
