<template>
  <div class="select-analysis-type">
    <h3 class="is-size-5 mb-4">
      What type of analysis do you want to carry out?
    </h3>

    <div class="columns">
      <div class="column">
        <div class="card-button app-promo--grey">
          <a
            class="card-button__link-wrapper"
            href="#/analysis/influencers"
            @click="emitAnalysisType('categorical')"
          >
            <img
              class="card-button__img"
              src="https://res.cloudinary.com/dayqxxsip/image/upload/v1603884319/App%20Images/categorical_i8utze.jpg"
              alt="Classification analysis"
              rel="preload"
              style="height: 300px"
            />
            <div class="card-button__content">
              <h3 class="card-button__heading">Categorical</h3>
              <p class="card-button__description">
                What influences this to be A or B? Segments the data to uncover
                influencers on the target variable and target value for
                classification models.
              </p>
            </div>
          </a>
        </div>
      </div>
      <div class="column">
        <div class="card-button app-promo--grey">
          <a
            class="card-button__link-wrapper"
            href="#/analysis/influencers"
            @click="emitAnalysisType('continuous')"
          >
            <img
              class="card-button__img"
              src="https://res.cloudinary.com/dayqxxsip/image/upload/v1603884365/App%20Images/continuous_q8yggc.jpg"
              alt="Regression analysis"
              rel="preload"
              style="height: 300px"
            />
            <div class="card-button__content">
              <h3 class="card-button__heading">Continuous</h3>
              <p class="card-button__description">
                What influences this to increase or decrease? Segments the data
                to uncover influencers on the target variable for regression
                models.
              </p>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "selectAnalysis",
  methods: {
    emitAnalysisType(type) {
      this.$emit("analysisType", type);
    }
  },
};
</script>

<style scoped>
.text-bottom {
  vertical-align: bottom;
}

.dropdown-item:focus {
  background-color: white;
}

.is-active {
  background-color: #1d70b8 !important;
}

.card-button {
  margin-bottom: 36px;
  width: 100%;
}

.card-button__link-wrapper {
  background-color: #fff;
  border: 1px solid transparent;
  box-shadow: 0 4px 0 0 #d8dde0;
  display: block;
  height: 100%;
  position: relative;
  text-decoration: none;
  color: #005ea5;
}

.card-button__link-wrapper:hover {
  background-color: #fff;
  color: #005eb8;
}

.card-button__link-wrapper:hover .card-button__heading {
  color: #7c2855;
}

.card-button__link-wrapper:focus {
  background-color: #fff;
  box-shadow: 0 4px 0 0 #d8dde0;
}

.card-button__link-wrapper:focus .card-button__heading {
  background-color: #ffeb3b;
  box-shadow: 0 -2px #ffeb3b, 0 4px #212b32;
  color: #212b32;
  outline: 4px solid transparent;
  text-decoration: none;
}

.card-button__link-wrapper:active {
  background-color: #fff;
  box-shadow: none;
  top: 4px;
}

.card-button__link-wrapper:active .card-button__heading {
  background: 0 0;
  box-shadow: none;
}

.card-button__link-wrapper:active .card-button__heading,
.card-button__link-wrapper:hover .card-button__heading {
  text-decoration: none;
}

.card-button__img {
  border-bottom: 1px solid #f0f4f5;
  display: block;
  width: 100%;
}

@media print {
  .card-button__img {
    display: none;
  }
}

.card-button__heading {
  font-weight: 600;
  font-size: 20px;
  font-size: 1.25rem;
  line-height: 1.4;
  display: inline-block;
  margin-bottom: 16px;
  text-decoration: underline;
}

@media (min-width: 40.0625em) {
  .card-button__heading {
    font-size: 24px;
    font-size: 1.5rem;
    line-height: 1.33333;
  }
}

@media print {
  .card-button__heading {
    font-size: 18pt;
    line-height: 1.15;
  }
}

.card-button__content {
  padding: 24px;
}

.card-button__content > :first-child {
  margin-top: 0;
}

.card-button__content > :last-child {
  margin-bottom: 0;
}

@media (min-width: 40.0625em) {
  .card-button__content {
    padding: 32px;
  }
}

.card-button__description {
  color: #4c6272;
}

.card-button--small .card-button__heading {
  font-size: 16px;
  font-size: 1rem;
  line-height: 1.5;
}

@media (min-width: 40.0625em) {
  .card-button--small .card-button__heading {
    font-size: 19px;
    font-size: 1.1875rem;
    line-height: 1.47368;
  }
}

@media print {
  .card-button--small .card-button__heading {
    font-size: 14pt;
    line-height: 1.15;
  }
}

.card-button--small .card-button__description {
  font-size: 14px;
  font-size: 0.875rem;
  line-height: 1.71429;
}

@media (min-width: 40.0625em) {
  .card-button--small .card-button__description {
    font-size: 16px;
    font-size: 1rem;
    line-height: 1.5;
  }
}

@media print {
  .card-button--small .card-button__description {
    font-size: 14pt;
    line-height: 1.2;
  }
}

.card-button-group {
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 36px;
}

@media (max-width: 48.0525em) {
  .card-button-group {
    margin-bottom: 28px;
  }
}

.card-button-group__item {
  display: flex;
}

@media (max-width: 48.0525em) {
  .card-button-group__item {
    flex: 0 0 100%;
  }
}

@media (max-width: 48.0525em) {
  .card-button-group__item {
    margin-bottom: 28px;
  }

  .card-button-group__item:last-child {
    margin-bottom: 0;
  }
}

.card-button-group__item .card-button {
  margin-bottom: 0;
}
</style>
