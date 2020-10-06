<template>
  <section>
    <div class="columns">
      <div class="column">
        <div class="has-text-left">
          <h1 class="is-size-1 has-text-weight-bold content">{{ msg }}</h1>
          <p class="content">
            An analytics project starts with trying to understand the business
            problem.
            <span class="has-text-weight-bold">Explore Your Data</span> assists
            with data understanding, preparation, and validation.
          </p>
          <p class="content">
            The sections that
            follow in the cross-industry standard process for data mining (CRISP-DM) are 
            modelling, evaluation and deployment. The section below has useful resources for
            each of these three key areas.
          </p>
          <h3 class="is-size-4 has-text-weight-bold">Modelling</h3>
          <div class="content">
            <ul>
              <li><a href="https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/871178/A_guide_to_using_AI_in_the_public_sector__web_version_.pdf" class="link" target="_blank">Using AI in the public sector</a></li>
              <li><a href="https://scikit-learn.org/stable/" class="link" target="_blank">Scikit-learn and Python</a></li>
              <li><a href="https://www.tidymodels.org/" class="link" target="_blank">Tidymodels and R</a></li>
            </ul>
          </div>
          <h3 class="is-size-4 has-text-weight-bold">Evaluation</h3>
          <div class="content">
            <ul>
              <li>
                <a href="https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234" class="link" target="_blank">
                Evaluating machine learning algorithms</a>
              </li>
              <li>
                <a href="https://towardsdatascience.com/how-to-best-evaluate-a-classification-model-2edb12bcc587" class="link" target="_blank">
                Evaluating classification models</a>
              </li>
              <li>
                <a href="https://medium.com/acing-ai/how-to-evaluate-regression-models-d183b4f5853d" class="link" target="_blank">
                Evaluating regression models</a>
              </li>
            </ul>
          </div>
          <h3 class="is-size-4 has-text-weight-bold">Deployment</h3>
          <div class="content">
            <ul>
              <li>
                <a href="https://www.kdnuggets.com/2019/06/approaches-deploying-machine-learning-production.html" class="link" target="_blank">
                Overview of deploying machine learning to production</a>
              </li>
              <li>
                <a href="https://www.analyticsvidhya.com/blog/2017/09/machine-learning-models-as-apis-using-flask/" class="link" target="_blank">
                Deploy to Flask Web API</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="column">
        <b-image
          src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/CRISPDM-Extended-Majid.png/749px-CRISPDM-Extended-Majid.png"
          placeholder="https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png"
          webp-fallback=".jpg"
          class="mt-6"
        >
        </b-image>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "next-steps",
  data() {
    return {
      filename: sessionStorage["sessionId"],
      timestamp: Date.now(),
    };
  },
};
</script>

<style>
</style>
