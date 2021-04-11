<template>
  <v-container>
    <v-alert type="info">{{ JSON.stringify(this.posts) }}</v-alert>
    <v-row>
      <v-col cols="12" sm="4" md="4" lg="4" xl="4">
        <v-card
          tile
          elevation="8"
          color="red"
          class="white--text pa-4 mb-4 text-center"
        >
          <v-card-subtitle class="font-weight-bold">
            Indie Developer's Website.
          </v-card-subtitle>
          <v-card-title
            class="justify-center font-weight-bold"
            style="font-size: 1.4rem"
          >
            Welcome to Kreimben.com!
          </v-card-title>
        </v-card>
      </v-col>

      <!-- Description -->
      <v-col cols="12" sm="8" md="8" lg="8" xl="8">
        <v-card
          tile
          style="font-size: 1.4rem"
          class="pa-4 text--primary font-weight-bold"
          color="green darken-2"
        >
          <p class="white--text">I code what I want.</p>
          <p class="white--text">iOS, macOS, Fullstack Developer.</p>
        </v-card>
      </v-col>

      <!-- image -->
      <v-col cols="12" sm="6" md="6" lg="6" xl="4">
        <v-card tile color="amber accent-4" class="pa-6 mb-4 text--primary">
          <p class="white--text pb-1 font-weight-bold">
            Today's Photo from NASA.
          </p>
          <v-skeleton-loader
            class="mx-auto"
            min-height="500"
            type="image"
            v-if="url === ''"
          />
          <v-img :src="url" />
        </v-card>
      </v-col>

      <!-- Posts (max 9) -->
      <v-col
        cols="12"
        sm="6"
        md="6"
        lg="6"
        xl="4"
        v-for="(post, index) in posts"
        :key="index"
      >
        <v-card
          tile
          color="blue"
          class="pa-4 text--primary text-center"
          @click="$router.push({ path: '/test_page' })"
        >
          <v-card-title
            class="font-weight-bold white--text justify-center"
            style="font-size: 1.6rem"
            >{{ post.title }}</v-card-title
          >

          <!-- Category -->
          <v-hover v-slot="{ hover }" open-delay="100">
            <v-card
              tile
              outlined
              max-width="80"
              :elevation="hover ? 2 : 0"
              color="indigo accent-2"
              class="mx-auto py-1 white--text rounded-xl"
              @click="$router.push(`/tags/${1+1}/`)"
            >
              {{ 1+1 }}
            </v-card>
          </v-hover>

          <!-- Description -->
          <v-card-subtitle class="white--text">{{
            post.description
          }}</v-card-subtitle>

          <!-- Date -->
          <v-card
            tile
            outlined
            width="110"
            color="indigo accent-2"
            class="mx-auto py-1 justify-center rounded-xl"
            style="color: white"
          >
            {{ this.getOnlyDate(post.createdAt) }}
          </v-card>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import mainImage from "../api/FetchImage";
import { FetchPostsFromMainView } from "../api/FetchPosts";

@Component
export default class MainView extends Vue {
  url = "";
  posts = null;

  async mounted(): Promise<void> {
    this.url = await mainImage();
    this.posts = await FetchPostsFromMainView("_limit=9");
  }

  public getToken(): string {
    if (Vue.prototype.$token) {
      return Vue.prototype.$token;
    } else {
      return "N/A";
    }
  }

  public getOnlyDate(date: string): string {
    const separate = date.split("T");

    return separate[0];
  }
}
</script>
