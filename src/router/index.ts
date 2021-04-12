import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";

import MainView from "../views/MainView.vue";
import AboutMeView from "../views/AboutMeView.vue";
import ManagePostsView from "../views/ManagePostsView.vue";
import LoginView from "../views/LoginView.vue";
import CategoriesView from "@/views/CategoriesView.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    component: MainView,
  },
  {
    path: "/categories",
    component: CategoriesView,
  },
  {
    path: "/aboutme",
    component: AboutMeView,
  },
  {
    path: "/login",
    component: LoginView,
  },
  {
    path: "/manage_posts",
    component: ManagePostsView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
