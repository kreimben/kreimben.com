import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";

import MainView from "../views/MainView.vue";
import AboutMeView from "../views/AboutMeView.vue";
import TagsView from "../views/TagsView.vue";
import ManagePostsView from "../views/ManagePostsView.vue";

import { authGuard } from "../auth/authGuard";

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
  {
    path: "/manage_posts",
    component: ManagePostsView,
    beforeEnter: authGuard
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
