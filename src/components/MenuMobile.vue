<template>
  <v-app-bar app fixed color="white">
    <router-link to="/">
      <v-img src="../../public/resized_favicon.png" contain />
    </router-link>

    <v-spacer />

    <v-app-bar-nav-icon @click="drawer = true" app> </v-app-bar-nav-icon>

    <v-navigation-drawer app v-model="drawer" absolute right>
      <v-list nav>
        <v-list-item
          v-for="(element, index) in testMenuItems"
          :key="index"
          @click="$router.push({ path: element.path })"
        >
          <v-list-item-title>{{ element.title }}</v-list-item-title>
        </v-list-item>
      </v-list>

      <v-btn
        v-if="this.$auth.user !== undefined"
        @click="$router.push({ path: '/manage_posts' })"
        text
        >Manage Posts</v-btn
      >

      <v-btn icon>
        <v-icon v-if="!$auth.isAuthenticated">mdi-login</v-icon>
        <v-icon v-else>mdi-logout</v-icon>
      </v-btn>

      <div class="gcse-searchbox-only" />
    </v-navigation-drawer>
  </v-app-bar>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({})
export default class MenuMobile extends Vue {
  drawer = false;

  testMenuItems = [
    {
      title: "Home",
      path: "/",
    },
    {
      title: "Tags",
      path: "/tags",
    },
    {
      title: "About Me",
      path: "/aboutme",
    },
  ];
}
</script>
