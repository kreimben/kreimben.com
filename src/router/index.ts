import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";

import MainView from "@/views/MainView.vue";
import AboutMeView from "@/views/AboutMeView.vue";
import ManagePostsView from "@/views/ManagePostsView.vue";
import LoginView from "@/views/LoginView.vue";
import CategoriesView from "@/views/CategoriesView.vue";
import CategoryView from "@/views/CategoryView.vue";
import PostView from "@/views/PostView.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
    {
        path: "/",
        component: MainView,
    },
    {
        path: "/posts/:id",
        component: PostView,
    },
    {
        path: "/categories",
        component: CategoriesView,
    },
    {
        path: "/categories/:id",
        component: CategoryView,
    },
    {
        path: "/login",
        component: LoginView,
    },
    {
        path: "/manage_posts",
        component: ManagePostsView,
    },

    {
        path: "*",
        redirect: (to) => {
            return '/';
        },
    },
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router;
