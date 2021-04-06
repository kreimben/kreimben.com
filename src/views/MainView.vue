<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="4" md="4" lg="4" xl="4">
        <v-card
          tile
          elevation="8"
          color="deep-orange darken-1"
          class="white--text pa-4 mb-4"
        >
          <v-card-subtitle class="font-weight-bold">
            Indie Developer's Website.
          </v-card-subtitle>
          <v-card-title class="font-weight-black" style="font-size: 1.4rem">
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
          color="red"
        >
          <p class="white--text">I code what I want.</p>
          <p class="white--text">iOS, macOS, Fullstack Developer.</p>
        </v-card>
      </v-col>

      <!-- image -->
      <v-col cols="12" sm="6" md="6" lg="6" xl="6">
        <v-card tile color="amber accent-4" class="pa-6 mb-4 text--primary">
          <p class="white--text pb-1 font-weight-bold">
            Today's Photo from NASA.
          </p>
          <v-skeleton-loader
            class="mx-auto"
            min-height="500"
            type="image"
            v-if="url === null"
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
        xl="6"
        v-for="post in testPosts"
        :key="post"
      >
        <v-card
          tile
          color="blue"
          class="pa-4 text--primary"
          @click="$router.push({ path: '/sdf' })"
        >
          <v-card-title
            class="font-weight-bold white--text"
            style="font-size: 1.6rem"
            >{{ post.title }}</v-card-title
          >
          <v-card-subtitle class="white--text">{{ post.desc }}</v-card-subtitle>
          <v-card
            tile
            width="110"
            color="light-blue accent-1"
            class="font-weight-bold pa-2"
            style="color: white"
            >{{ getOnlyDate(post.date) }}</v-card
          >
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

import mainImage from "../api/FetchImage";

@Component
export default class MainView extends Vue {
  url = null;

  async created() {
    this.url = await mainImage();
    console.log(`this is result: ${this.url}`);
  }

  public getOnlyDate(date: string): string {
    const separate = date.split(":");

    return separate[0];
  }

  testPosts = [
    {
      title: "First post",
      desc: "alskdjfjlskdj",
      date: "2021-03-21:04:56",
    },
    {
      title: "Second post",
      desc: "sldkjlknamlsdkfj",
      date: "2021-03-21:04:56",
    },
    {
      title: "Third post",
      desc: "sldkjlknamlsdkfj",
      date: "2021-03-21:04:56",
    },
    {
      title: "Fourth post",
      desc: "sldkjlknamlsdkfj",
      date: "2021-03-21:04:56",
    },
    {
      title: "Fivth post",
      desc: "sldkjlknamlsdkfj",
      date: "2021-03-21:04:56",
    },
    {
      title: "Sixth post",
      desc: "sldkjlknamlsdkfj",
      date: "2021-03-21:04:56",
    },
    {
      title: "Seventh post",
      desc: "sldkjlknamlsdkfj",
      date: "2021-03-21:04:56",
    },
  ];
}
</script>
