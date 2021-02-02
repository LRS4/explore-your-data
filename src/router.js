import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Api from './views/Api.vue'
import Upload from './views/Upload.vue'
import Analysis from './views/Analysis.vue'
import OverviewTab from "@/components/tabs/OverviewTab.vue";
import SampleTab from "@/components/tabs/SampleTab.vue";
import UnivariateTab from "@/components/tabs/UnivariateTab.vue";
import BivariateTab from "@/components/tabs/BivariateTab.vue";
import MissingDataTab from '@/components/tabs/MissingDataTab.vue';
import CorrelationTab from '@/components/tabs/CorrelationTab.vue';
import PivotTab from '@/components/tabs/PivotTab.vue';
import InfluencersTab from '@/components/tabs/InfluencersTab/InfluencersTab.vue';
import NextStepsTab from '@/components/tabs/NextStepsTab.vue';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    },
    {
      path: '/upload',
      name: 'upload',
      component: Upload
    },
    {
      path: '/analysis',
      name: 'analysis',
      component: Analysis,
      children: [
        {
          path: 'overview',
          component: OverviewTab
        },
        {
          path: 'sample',
          component: SampleTab
        },
        {
          path: 'variables',
          component: UnivariateTab
        },
        {
          path: 'interactions',
          component: BivariateTab
        },
        {
          path: 'correlation',
          component: CorrelationTab
        },
        {
          path: 'crosstab',
          component: PivotTab
        },
        {
          path: 'missing',
          component: MissingDataTab
        },
        {
          path: 'influencers',
          component: InfluencersTab
        },
        {
          path: 'next-steps',
          component: NextStepsTab
        }
      ]
    }
  ]
})
