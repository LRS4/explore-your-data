<template>
  <div class="has-text-left">
    <h1 class="is-size-1 has-text-weight-bold content">{{ msg }}</h1>
    <p class="content">
      <span class="has-text-weight-bold">Explore Your Data</span> provides automated exploratory data analysis as a service.
      This can be used by individuals and organisations to better understand your datasets,
      to support the start of new data projects.
    </p>
    <p class="content">
      Exploratory data analysis (EDA) is an approach to analyzing datasets to summarise their main characteristics,
      often with visual methods. A statistical model can be used or not, but primarily EDA is for seeing what the data
      can tell us beyond the formal modeling or hypothesis testing task.
    </p>
    <h3 class="is-size-4 has-text-weight-bold">Use this service to:</h3>
    <div class="content">
      <ul>
        <li>Get a basic understanding of any dataset you upload</li>
        <li>Carry out guided data exploration</li>
        <li>Get ideas and suggestions on how to develop your data project</li>
      </ul>
    </div>
    <h3 class="is-size-4 has-text-weight-bold content">Before you start</h3>
    <p class="content">
      You'll need your dataset in CSV (comma-seperated values) format.
      Currently Explore Your Data only allows CSV files as uploads.
      <a class="link" 
        href="https://support.microsoft.com/en-us/office/save-a-workbook-to-text-format-txt-or-csv-3e9a9d6c-70da-4255-aa28-fcacf1f081e6"
        target="_blank">
        How to store data as a CSV file?
      </a>
    </p>
    <p class="content">
      The dataset uploaded will need to be understandable. For example, naming a column 'Date of Birth' or 'DateOfBirth' is
      easier to understand than 'dob'.
    </p>
    <b-button
      class="is-success start-button has-text-weight-bold"
      size="is-large"
      :rounded="false"
      tag="router-link"
      :to="{ path: '/api' }"
    >Upload data</b-button>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
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

.start-button {
  background-color: #00703c !important;
}

.start-button:hover {
  background-color: #00703cf3 !important;
}

.start-button:active {
  border: 3px solid;
  border-color: #ffdd00 !important;
}
</style>
