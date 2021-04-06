import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";

import MainView from "../views/MainView.vue";
import AboutMeView from "../views/AboutMeView.vue";
import TagsView from "../views/TagsView.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    component: MainView,
  },
  {
    path: "/tags",
    component: TagsView,
  },
  {
    path: "/aboutme",
    component: AboutMeView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
