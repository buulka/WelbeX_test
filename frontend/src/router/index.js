import Vue from 'vue'
import Router from 'vue-router'
import Items from '@/components/Items'
import Vuelidate from "vuelidate";

Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Items',
      component: Items,
    },
  ],
  mode: 'history',
});
